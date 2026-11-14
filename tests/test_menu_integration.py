"""Run the package API as a user would from a fresh Python process."""

import json
from pathlib import Path
import subprocess
import sys

import pytest

from fridgelin import menu, price
from fridgelin import menus


PROGRAM = """
import json
import sys
from fridgelin import menu, price

request = json.load(sys.stdin)
food = request["food"]
level = request["level"]
options = request["options"]
try:
    result = {"dollars": price(food, level), "menu": menu(food, level=level, **options)}
except (TypeError, ValueError) as error:
    result = {"error": type(error).__name__, "message": str(error)}
print(json.dumps(result, ensure_ascii=True))
"""


def isolated_request(folder: Path, food, level, **options):
    request = json.dumps({"food": food, "level": level, "options": options})
    result = subprocess.run(
        [sys.executable, "-c", PROGRAM],
        input=request,
        text=True,
        capture_output=True,
        check=True,
        cwd=folder,
        timeout=15,
    )
    assert result.stderr == ""
    return json.loads(result.stdout)


def test_original_package_exports_are_the_menu_module_functions():
    assert menu is menus.menu
    assert price is menus.price


@pytest.mark.parametrize("seed", [-7, 0, 10**12])
def test_importing_from_another_directory_reproduces_the_seeded_menu(tmp_path, seed):
    food = [" 豆腐 ", "EGG"]
    result = isolated_request(tmp_path, food, 2, courses=2, seed=seed, width=40)
    assert result["dollars"] == 44.99
    assert result["menu"] == menu(food, 2, 2, 40, seed)


def test_default_unseeded_menu_can_be_returned_as_plain_text(tmp_path):
    result = isolated_request(tmp_path, ["rice"], 3)
    rows = result["menu"].splitlines()
    assert result["dollars"] == 68.49
    assert rows[0] == "Tonight's Tasting Menu"
    assert len(rows) == 5
    assert rows[-1].endswith("$205.47")


@pytest.mark.parametrize(("food", "level", "options", "kind", "field"), [
    ([None], 1, {}, "TypeError", "Ingredient"),
    ([], 3, {}, "ValueError", "Ingredients"),
    (["rice"], 1, {"seed": False}, "TypeError", "Seed"),
    (["rice"], 1, {"courses": 7}, "ValueError", "Courses"),
    (["rice"], 6, {}, "ValueError", "Level"),
])
def test_public_package_errors_survive_a_fresh_import(tmp_path, food, level, options, kind, field):
    result = isolated_request(tmp_path, food, level, **options)
    assert result["error"] == kind
    assert field in result["message"]
