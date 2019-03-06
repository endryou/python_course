from sys import argv
import matplotlib.pyplot as plt


if len(argv) == 2:
    print('The input is:', argv[1],
          "\nCreating a plot of given length...")

plot_len = argv[1]

circle1 = plt.Circle((0, 0), radius=plot_len, color='g')
circle2 = plt.Circle((0.5, 0.5), radius=0.8*plot_len, color='blue')
circle3 = plt.Circle((-0.5, -0.5), radius=1.2*plot_len, color='r')
fig, ax = plt.subplots()
plt.axis('scaled')
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
plt.show()
