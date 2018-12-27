# -*- encoding: utf-8


def condense_into_single_line(text):
    """
    Remove all the newlines from a block of text, compressing multiple
    lines of HTML onto a single line.  Used as a Jinja2 filter.
    """
    lines = [line.lstrip() for line in text.split('\n')]
    return ''.join(lines)
