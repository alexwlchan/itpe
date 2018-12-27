#!/usr/bin/env python
# -*- encoding: utf-8

from hypothesis import given
from hypothesis.strategies import text
import pytest

from itpe.jinja_helpers import condense_into_single_line, get_jinja2_template

@given(text())
def test_condense_into_single_line_removes_newlines(xs):
    assert "\n" not in condense_into_single_line(xs)


@given(text())
def test_condense_into_single_line_is_stable(xs):
    condensed_xs = condense_into_single_line(xs)
    assert condense_into_single_line(condensed_xs) == condensed_xs


@pytest.mark.parametrize("text, expected_output", [
    ("foo bar", "foo bar"),
    ("foo \nbar", "foo bar"),
    ("foo \nbar\n", "foo bar"),
    (" foo \nbar\n", "foo bar"),
])
def test_condense_into_single_line_strips_from_left(text, expected_output):
    assert condense_into_single_line(text) == expected_output


def test_can_get_template():
    get_jinja2_template()
