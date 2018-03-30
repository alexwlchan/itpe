# -*- encoding: utf-8

import os

import pytest
from schema import SchemaError

from itpe import cli


@pytest.fixture
def example_file(tmpdir):
    curdir = os.path.abspath(os.curdir)
    try:
        os.chdir(tmpdir)
        open('example.csv', 'w').write('')
        yield
    finally:
        os.chdir(curdir)


@pytest.mark.parametrize('argv, expected_message', [
    (['--input', 'doesnotexist.csv'],
     "--input='doesnotexist.csv' should be readable"),

    (['--input', 'example.csv', '--width', '-5'],
     "--width='-5' should be a positive integer"),
    (['--input', 'example.csv', '--width', '6xx'],
     "--width='6xx' should be a positive integer"),

    (['--input', 'example.csv', '--output', 'example.csv'],
     "--output='example.csv' already exists!"),
])
def test_errors_are_helpful(example_file, argv, expected_message):
    with pytest.raises(SchemaError) as err:
        cli.get_args(argv)
    assert str(err.value) == expected_message


def test_width_arg_is_converted_to_int():
    parsed_args = cli.get_args(['--input', 'tox.ini', '--width', '50'])
    assert parsed_args['--width'] == 50


def test_guesses_sensible_output_if_not_provided(example_file):
    parsed_args = cli.get_args(['--input', 'example.csv'])
    assert parsed_args['--output'] == 'example.html'
