import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys


def my_checker(x):
    if x == 0:
        print("You cannot do math using zero! Enter a number")
        sys.exit()
    try:
        val = float(x)
        print("Yes, it's a float number")
    except ValueError:
        print("That's not a float number!\nPlease entemy_checker(x)r a float!")
        sys.exit()
    return True


value = input("enter a value: ")
my_checker(value)
value = float(value)
x_k = np.linspace(-1.5 * np.pi, 3 * np.pi, 201)
y_k = np.linspace(-1.5 * np.pi, 3 * np.pi, 201)
X, Y = np.meshgrid(x_k, y_k)
R = np.sqrt(X**2+Y**2)
Z = np.cos(R)**value*np.exp(-0.1**R)
ax = Axes3D(plt.figure(figsize=(8,5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.show()