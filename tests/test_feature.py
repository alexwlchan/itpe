#!/usr/bin/env python
# -*- encoding: utf-8

import os
import sys
import tempfile

from itpe import main


def test_command_line():
    sys.argv = ["itpe", "--input", "tests/example.csv"]
    main()
    assert os.path.exists("tests/example.html")
    os.unlink("tests/example.html")


def test_command_line_with_explicit_output():
    out_path = os.path.join(tempfile.mkdtemp(), "example.html")
    sys.argv = ["itpe", "--input", "tests/example.csv", "--output", out_path]
    main()
    assert os.path.exists(out_path)
    os.unlink(out_path)
