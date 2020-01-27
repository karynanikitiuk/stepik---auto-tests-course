import pytest

@pytest.mark.xfail(strict=True)
#@pytest.mark.xfail(condition=True, reason=None, raises="this bug right now", strict=True, run=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False



#pytest -rx -v test_xfail.py  консоль