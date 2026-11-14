import subprocess
import sys
from fridgelin import name





def run(args):
    return subprocess.run([sys.executable, "-m", "fridgelin"] + args, capture_output=True, text=True)




def test_name_only():
    out =run(["rice", "--seed", "1", "--only", "name"])
    assert out.returncode==0
    assert out.stdout==name(["rice"], 3, 1) + "\n"


def test_everything():
    out =run(["rice", "egg", "--seed", "1"])
    assert out.returncode==0
    assert len(out.stdout.strip().split("\n\n"))==4
    assert "Tonight's Tasting Menu" in out.stdout
    assert "-- Percival Crumb, 3/5" in out.stdout


def test_one_part_each():
    for part in ["menu", "review", "drink"]:
        out = run([ "rice", "egg", "--seed", "2", "--only", part])
        assert out.returncode==0
        assert "\n\n" not in out.stdout.strip()





def test_bad_options():
    
    out=run(["rice", "--courses", "7"])
    assert out.returncode == 2
    assert out.stderr.startswith("fridgelin: ")

    out=run(["rice", "--level", "9"])
    assert out.returncode == 2

    out=run(["rice", "--budget", "rich"])
    assert out.returncode == 2

    out=run(["", "--seed", "1"])
    assert out.returncode == 2
    assert out.stdout == ""




