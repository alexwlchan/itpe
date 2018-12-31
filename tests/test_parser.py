# -*- encoding: utf-8

import os

import pytest

from itpe import get_podfics, Podfic


def test_can_get_podfics():
    r = get_podfics("tests/example.csv")
    assert len(r) == 1
    assert r[0] == Podfic(
        "tw/from_user",
        "dw/for_user",
        "https://example.org/cover_art.jpg",
        "dw/cover_artist",
        "dw/editor",
        "My Great Title",
        "https://ao3.org/my_fic",
        "tw/author",
        "Harry Potter",
        "ron/hermione",
        "no warnings",
        "1:30",
        "https://example.org/file.mp3",
        "https://example.org/file.m4b",
        "dw/podbook_compiler",
    )


@pytest.mark.parametrize('path', ["too_many_columns.csv", "not_enough_columns.csv"])
def test_wrong_number_of_columns_is_valueerror(path):
    with pytest.raises(ValueError):
        get_podfics(os.path.join("tests", path))


def test_can_read_csv_with_utf8():
    r = get_podfics("tests/example_with_utf8.csv")
    assert len(r) == 2
    assert r[1].from_user == u"tw/fröm_user"
    assert r[1].for_user == u"dw/for_usér"
