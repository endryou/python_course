import numpy as np
import sys


def count_field(figure, x, y=None):
    figure = figure.lower()
    try:
        x = float(x)

        if y is not None:
            y = float(y)
            if y < 0 or y == 0:
                sys.exit("y cannot be below or equal zero. Program stops")
        if x < 0 or y == 0:
            sys.exit("x cannot be below or equal zero. Program stops")
    except ValueError:
        sys.exit("Wrong value. Please enter float or integer. Program stops")
    if figure == 'circle':
        field = np.pi * x ** 2
    elif figure == 'rectangle':
        field = x * y
    elif figure == 'triangle':
        field = 0.5 * x * y
    elif figure == 'rhombus':
        field = 0.5 * x * y
    else:
        sys.exit("Wrong figure. Program stops")
    return figure, field


# print(count_field('rhombus', 5, 4))