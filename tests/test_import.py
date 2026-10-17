import magpy_lite


def test_version():
    assert isinstance(magpy_lite.__version__, str)
