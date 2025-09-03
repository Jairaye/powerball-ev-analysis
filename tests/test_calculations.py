from analysis.utils import after_tax

def test_after_tax():
    assert round(after_tax(100, 0.25), 2) == 75.00
