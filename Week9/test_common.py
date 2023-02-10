import pytest
from common import common_chars


def test_empty_sets():
    assert common_chars('', '') == (0, 0), 'empty strs'


def test_different_cases():
    assert common_chars('abc', 'ABC') == (0, 3), 'strings of different chars'
    assert common_chars('abcx', 'abcX') == (3, 4)


if __name__ == "__main__":
    pytest.main(["test_common.py"])
