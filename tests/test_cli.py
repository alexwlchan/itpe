# -*- encoding: utf-8

import pytest
from schema import SchemaError

from itpe import cli


@pytest.mark.parametrize('argv, expected_message', [
    (['--input', 'doesnotexist.csv'],
     "--input='doesnotexist.csv' should be readable"),

    (['--input', 'tox.ini', '--width', '-5'],
     "--width='-5' should be a positive integer"),
    (['--input', 'tox.ini', '--width', '6xx'],
     "--width='6xx' should be a positive integer"),

    (['--input', 'tox.ini', '--output', 'tox.ini'],
     "--output='tox.ini' already exists!"),
])
def test_errors_are_helpful(argv, expected_message):
    with pytest.raises(SchemaError) as err:
        cli.get_args(argv)
    assert str(err.value) == expected_message


def test_width_arg_is_converted_to_int():
    parsed_args = cli.get_args(['--input', 'tox.ini', '--width', '50'])
    assert parsed_args['--width'] == 50
