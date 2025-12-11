import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

import app

def test_add():
    assert app.add(5, 6) == 11

def test_add2():
    assert app.add(5, 6) != 10
