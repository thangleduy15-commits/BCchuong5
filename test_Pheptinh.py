from Pheptinh import cong, tru, nhan, chia

def test_cong():
    assert cong(2, 3) == 5
    assert cong(-1, 1) == 0
    assert cong(0, 0) == 0

def test_tru():
    assert tru(5, 3) == 2
    assert tru(0, 0) == 0
    assert tru(-1, -1) == 0

def test_nhan():
    assert nhan(2, 3) == 6
    assert nhan(0, 0) == 0
    assert nhan(-1, 1) == -1

def test_chia():
    assert chia(6, 2) == 3
    assert chia(0, 1) == 0
    try:
        chia(1, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass