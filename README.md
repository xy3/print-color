# print-color

Print Color is a minimalist approach to terminal color printing in Python. It is a wrapper around the `print()` function, and simply allows you to provide extra optional parameters such as:
- tag
- tag_color
- color
- background
- format

It aims to be a customizable logger for your applications, and makes formatting warnings, info messages and errors a breeze.

---

## Information

This project has no dependencies.

Check out this project on [PyPi here](https://pypi.org/project/print-color/).

Colors:
```
purple
blue
green
yellow
red
magenta
cyan
white
```

### Parameter values:

- `tag`
    - any string
- `tag_color`
    - color
- `color`
    - color
- `background`
    - color
- `format`
    - bold
    - underline
    - blink

### Installing

```
pip3 install print-color
```

### Requirements

- python 3.5^

### Usage

```
from print_color import print

print("Hello world", tag='success', tag_color='green', color='white')
```

![Success tag](https://i.imgur.com/qmeYTkR.png)

```
print("Error detected", tag='failure', tag_color='red', color='magenta')
```

![Error tag](https://i.imgur.com/dksa03u.png)

```
print("Printing in color", color='green', format='underline', background='grey')
```

![Printing in color is easy](https://i.imgur.com/3sUTi8z.png)


## Contributing

Feel free to add or improve this project :) Just create a pull request and explain the changes you propose.
Note that as this is a very simple project, feature requests should be kept minimal - things like more colors, formats etc would be ideal.

## Credits

Built with [Python Poetry](https://python-poetry.org/).

### Contributers

- Theo ([@xy3](https://github.com/xy3))

