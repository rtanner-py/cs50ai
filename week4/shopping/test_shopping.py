import pytest 

from shopping import replaceMonth, replaceVisitorType

def test_replaceMonth_lower():
    assert replaceMonth('jan') == 0

def test_replaceMonth_upper():
    assert replaceMonth('JAN') == 0

def test_replaceMonth_mixed():
    assert replaceMonth('JaN') == 0

def test_replaceMonth_unknown():
    with pytest.raises(Exception) as e_info:
        replaceMonth('test')

def test_replaceVisitorType_returning():
    assert replaceVisitorType("Returning_Visitor") == 1

def test_replaceVisitorType_other():
    assert replaceVisitorType("false") == 0

def test_replaceVisitorType_blank():
    assert replaceVisitorType("") == 0