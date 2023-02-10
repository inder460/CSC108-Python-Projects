import pytest
import merge_dict as md


def test_d2_empty():
    d1 = {5: 3, 4: 2}
    d2 = {}
    d2_copy = {}
    expected_d1 = {5: 3, 4: 2}
    assert md.merge_dict(d1, d2) is None, 'None not returned '
    assert d1 == expected_d1, 'd2 empty'
    assert d2 == d2_copy, 'd2 was modified'


def test_cases():
    d1 = {5: 3, 4: 2}
    d2 = {4: 7, 6: 3}
    d2_copy = {4: 7, 6: 3}
    expected_d1 = {4: 9, 5: 3, 6: 3}
    assert md.merge_dict(d1, d2) is None, 'None not returned '
    assert d1 == expected_d1, 'd2 empty'
    assert d2 == d2_copy, 'd2 was modified'
