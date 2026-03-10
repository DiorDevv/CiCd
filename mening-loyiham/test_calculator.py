import pytest
from calculator import qoshish, ayirish, kopaytirish, bolish

def test_qoshish():
    assert qoshish(2, 3) == 5
    assert qoshish(-1, 1) == 0

def test_ayirish():
    assert ayirish(5, 3) == 2

def test_kopaytirish():
    assert kopaytirish(4, 3) == 12

def test_bolish():
    assert bolish(10, 2) == 5.0

def test_nolga_bolish():
    with pytest.raises(ValueError):
        bolish(5, 0)