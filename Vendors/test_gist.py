import pytest

def test_our_first_case():
    assert 1==1

@pytest.mark.skip
def test_skip():
    assert 1==1

@pytest.mark.skipif(4>2,reason="Condition Failed   ")
def test_skip_2():
    assert 1==2
