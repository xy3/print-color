import sys
from print_color import print
from io import StringIO

default_ending = "\x1b[0m\n"


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
