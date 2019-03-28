from __future__ import division
import random
import matplotlib.pyplot as plt
import numpy as np
import sys


def my_checker(x):

    try:
        val = float(x)
        print("Yes, it's a float number")
    except ValueError:
        print("That's not a float number!\nPlease entemy_checker(x)r a float!")
        sys.exit()
    return True


t = np.linspace(0, 2*np.pi, 65)
x = input("x radius for plot: ")
my_checker(x)
x = float(x)
if x < 0:
    print("radius cannot be below zero\nContinuing the code...")
else:
    x_ax = x*np.cos(t)
    y_ax = x*np.sin(t)
    plt.plot(x_ax, y_ax, color='r')
    plt.grid()
    plt.show()

y = input("y radius for plot: ")
my_checker(y)
y = float(y)
if y < 0 or y == 0:
    print("radius cannot be below zero\nContinuing the code...")
else:
    x2_ax = y*np.cos(t)
    y2_ax = y*np.sin(t)
    plt.grid()
    plt.plot(x2_ax, y2_ax, color='b')
    plt.show()


def is_even(x):
    return x % 2 == 0


x = input("enter x to find x/y: ")
my_checker(x)
y = input("enter y to find x/y: ")
my_checker(y)
x, y = float(x), float(y)


def finding_xy(x, y):
    if y == 0:
        print("You cannot do math using zero! Enter a number")
        sys.exit()
    i = 1
    while True:
        if x % y == 0 and (is_even(x) and is_even(y)):
            return x, y, i
        else:
            i += 1
            x = random.randint(0, 100000)
            y = random.randint(0, 100000)


xf, yf, i = finding_xy(x, y)
print(f"FOUND after {i} iterations:\nx: {xf} \ny: {yf} \nx / y = {round((xf / yf), 2)}")


x = input("one line statement x: ")
my_checker(x)
y = input("one line statement y: ")
my_checker(y)
x, y = float(x), float(y)

print("X is divisible by Y") if x % y == 0 else print("X ise not divisible by Y")
