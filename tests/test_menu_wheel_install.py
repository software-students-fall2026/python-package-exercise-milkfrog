"""Check the public API from the exact wheel built out of the current checkout."""

import json
import os
from pathlib import Path
import subprocess
import sys
import zipfile

import pytest


PROBE = """
import json
from pathlib import Path
import sys

sys.path.insert(0, sys.argv[1])
import fridgelin
from fridgelin import menu, price
from fridgelin.menus import line

result = {
    "loaded_from": fridgelin.__file__,
    "dollars": price(["rice", "ketchup"], 2),
    "card": menu(["rice", "ketchup"], 2, 2, 40, 7),
    "long_row": line("R" * 50, 1.0, 40),
}
print(json.dumps(result))
"""


@pytest.fixture(scope="module")
def built_wheel(tmp_path_factory):
    """Build from the package users will receive and run probes from outside the checkout."""
    import fridgelin

    root = Path(fridgelin.__file__).resolve().parents[2]
    assert (root / "pyproject.toml").is_file(), "Run against the source checkout"
    folder = tmp_path_factory.mktemp("installed-menu")
    env = os.environ.copy()
    env.pop("PYTHONPATH", None)
    subprocess.run(
        [sys.executable, "-m", "build", "--wheel", "--outdir", str(folder)],
        cwd=root, env=env, check=True, capture_output=True, text=True, timeout=180,
    )
    wheel, = folder.glob("*.whl")
    return wheel


def test_wheel_contains_the_menu_api_and_its_runtime_dependencies(built_wheel):
    with zipfile.ZipFile(built_wheel) as archive:
        files = set(archive.namelist())
    assert {
        "fridgelin/__init__.py", "fridgelin/menus.py",
        "fridgelin/names.py", "fridgelin/helpers.py",
    } <= files
    assert not any(path.startswith("tests/") for path in files)


def test_isolated_interpreter_loads_the_built_wheel_and_reproduces_the_card(built_wheel):
    result = subprocess.run(
        [sys.executable, "-I", "-c", PROBE, str(built_wheel)],
        cwd=built_wheel.parent, check=True, capture_output=True, text=True, timeout=20,
    )
    output = json.loads(result.stdout)
    assert built_wheel.name in output["loaded_from"]
    assert output["dollars"] == 44.99
    rows = output["card"].splitlines()
    assert len(rows) == 4
    assert rows[0] == "Tonight's Tasting Menu"
    assert rows[1].endswith(" $30.99")
    assert rows[2].endswith(" $44.99")
    assert rows[3].endswith(" $75.98")
    assert output["long_row"] == "R" * 50 + "  $1.00"
