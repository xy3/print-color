import builtins
import sys


class PrintColor:
    colors = {
        "purple": '\033[95m',
        "blue": '\033[94m',
        "green": '\033[92m',
        "yellow": '\033[33m',
        "red": '\033[31m',
        "magenta": '\033[35m',
        "cyan": '\033[36m',
    }

    backgrounds = {
        'grey': '\033[40m', 'red': '\033[41m',
        'green': '\033[42m', 'yellow': '\033[43m',
        'blue': '\033[44m', 'magenta': '\033[45m',
        'cyan': '\033[46m', 'white': '\033[47m',
    }

    formats = {
        "bold": "\033[1m", "underline": "\033[4m", "blink": "\033[5m"
    }

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def print(self):
        color = self.kwargs.pop('color', None)
        back = self.kwargs.pop('background', None)
        format = self.kwargs.pop('format', None)
        tag = self.kwargs.pop('tag', None)
        tag_color = self.kwargs.pop('tag_color', None)
        file = self.kwargs.get('file', sys.stdout)
        result = ",".join(str(arg) for arg in self.args)

        if color:
            result = self.color(color) + result

        if tag:
            result = f"[{tag}] {result}"
            if tag_color:
                result = self.color(tag_color) + result
        # result += self.end
        if back:
            builtins.print(self.background(back), file=sys.stdout, end='')
        if format:
            builtins.print(self.format(format), file=sys.stdout, end='')
        result += self.end
        builtins.print(*result.split(','), **self.kwargs)

    def color(self, color):
        return self.colors.get(color, self.default_color)

    def background(self, back):
        return self.backgrounds.get(back, self.default_color)

    def format(self, format):
        if isinstance(format, str):
            return self.formats.get(format, self.default_color)
        elif isinstance(format, list, tuple):
            return ",".join(f for f in self.formats.get(f) for f in format)

    @property
    def end(self):
        return '\033[0m'

    @property
    def default_color(self):
        return '\033[0m'


def print(*args, **kwargs):
    printcolor = PrintColor(*args, **kwargs)
    printcolor.print()
