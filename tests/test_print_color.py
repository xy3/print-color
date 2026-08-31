import sys
from io import StringIO

from print_color import print

default_ending = "\x1b[0m\n"
color_green = "\x1b[92m"


def test_print_with_no_args():
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    print("test")
    assert capturedOutput.getvalue() == "test" + default_ending
    sys.stdout = sys.__stdout__


def test_print_with_tag():
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    print("test", tag="testTag")
    assert capturedOutput.getvalue() == "[testTag] test" + default_ending
    sys.stdout = sys.__stdout__


def test_print_leading_carriage_return_with_tag():
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    print("\rtest", tag="testTag")
    assert capturedOutput.getvalue() == "\r[testTag] test" + default_ending
    sys.stdout = sys.__stdout__


def test_print_leading_new_line_with_tag():
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    print("\ntest", tag="testTag")
    assert capturedOutput.getvalue() == "\n[testTag] test" + default_ending
    sys.stdout = sys.__stdout__


def test_print_leading_new_line_with_tag_and_color():
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    print("\ntest", tag="testTag", color="green")
    assert (
        capturedOutput.getvalue()
        == "\n[testTag] " + color_green + "test" + default_ending
    )
    sys.stdout = sys.__stdout__
