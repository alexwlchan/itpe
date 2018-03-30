# -*- encoding: utf-8
"""
Generate the HTML for the #ITPE master post.

Usage:
  itpe_generator.py --input <INPUT> [--output <OUTPUT>] [--width=<WIDTH>]
  itpe_generator.py (-h | --help)
  itpe_generator.py --version

Options:
  -h --help           Show this screen.
  --input=<INPUT>     CSV file containing the ITPE data.
  --output=<OUTPUT>   HTML file for writing the generated HTML.
  --width=<WIDTH>     Width of the cover art in px [default: 500].

"""

import os
import sys

import docopt
from schema import Schema, And, Or, Use, SchemaError


def get_args(argv):
    args = docopt.docopt(doc=__doc__, argv=argv)

    if args['--output'] is None:
        args['--output'] = os.path.splitext(args['--input'])[0] + '.html'

    schema = Schema({
        # These two keys get handled by docopt, so we just need to validate
        # that they've not been passed.
        '--help': False,
        '--version': False,

        # These are safety precautions: we shouldn't try to read an existing
        # file, and we shouldn't try to overwrite an existing file.  At some
        # point it might be nice to allow overriding the output rule with
        # '--force', but that adds unnecessary complication.
        '--input': And(
            lambda f: open(f, 'r'),
            error='--input=%r should be readable' % args['--input']
        ),
        '--output': And(
            lambda f: not os.path.exists(f),
            error='--output=%r already exists!' % args['--output']
        ),
        '--width': Or(
            None,
            And(
                Use(int),
                lambda w: w > 0,
                error='--width=%r should be a positive integer' % args['--width']
            )
        ),
    })

    args = schema.validate(args)

    return args
