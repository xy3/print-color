import sys
from print_color import print
from io import StringIO

capturedOutput = StringIO.StringIO()

@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    capturedOutput = StringIO.StringIO()
    sys.stdout = capturedOutput
    yield
    sys.stdout = sys.__stdout__


def test_print_with_no_args():
    print("test")
    assert capturedOutput.getvalue() == "test"


def test_print_with_tag():
    print("test", tag="testTag")
    assert capturedOutput.getvalue() == "[testTag] test"
