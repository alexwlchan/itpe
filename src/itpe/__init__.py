# -*- encoding: utf-8

import collections
import csv
import sys

from jinja2 import Environment, PackageLoader
from schema import SchemaError

from .cli import get_args
from .dreamwidth import render_user_links


# Headings for the CSV fields. These don't have to exactly match the spelling/
# spacing of the CSV, but the order should be the same. We define a set of
# heading names here so that we have consistent names to use in the script
HEADINGS = [
    'from_user',
    'for_user',
    'cover_art',
    'cover_artist',
    'editor',
    'title',
    'title_link',
    'authors',
    'fandom',
    'pairing',
    'warnings',
    'length',
    'mp3_link',
    'podbook_link',
    'podbook_compiler',
]

Podfic = collections.namedtuple('Podfic', HEADINGS)


def condense_into_single_line(text):
    """
    Remove all the newlines from a block of text, compressing multiple
    lines of HTML onto a single line.  Used as a Jinja2 filter.
    """
    lines = [line.lstrip() for line in text.split('\n')]
    return ''.join(lines)


def get_jinja2_template():
    """Set up the Jinja2 environment."""
    env = Environment(loader=PackageLoader('itpe', 'templates'),
                      trim_blocks=True)

    env.filters['condense'] = condense_into_single_line
    env.filters['userlinks'] = render_user_links

    template = env.get_template('podfic_template.html')

    return template


def get_podfics(input_file):
    """Read a CSV file and return a list of Podfic instances."""
    podfics = []

    with open(input_file, encoding='utf-8') as csvfile:
        itpereader = csv.reader(csvfile, delimiter=',')

        # Skip the first row, which only contains headings
        next(itpereader)

        for idx, row in enumerate(itpereader):
            print("Reading row %d..." % idx)

            # If we pass the incorrect number of arguments to Podfic,
            # it throws a TypeError.
            try:
                podfic = Podfic(*row)
            except TypeError:
                raise ValueError(
                    "Row %d has the wrong number of entries" % idx)

            podfics.append(podfic)

    return podfics


def main():
    try:
        args = get_args(sys.argv[1:], version='ITPE 2017.3')
    except SchemaError as err:
        import sys
        sys.exit(err)

    template = get_jinja2_template()

    # Get a list of podfics from the input CSV file
    podfics = get_podfics(args['<INPUT>'])

    # Turn those podfics into HTML
    podfic_html = (
        template.render(podfic=podfic, width=args['--width'] + 'px')
        for podfic in podfics
    )

    # Write the output HTML, with a <br /> between items to add space
    # in the rendered page.
    with open(args['--output'], 'w') as outfile:
        outfile.write('\n<br />\n'.join(podfic_html))

    print("HTML has been written to %s." % args['--output'])


if __name__ == '__main__':
    main()
