# TASKS (4p)
# 1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
# 2 ask the user for a number and print its factorial (1p)
# 3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of
# that element and its value (1p)
# 4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any
# chart of a given length. the length of a chart is the input to your script.
# The output is a plot (it doesn't matter if it's a y=x or  y=e^x+2x or y=|x| function, use your imagination)
# test your solution properly. Look how it behaves given different input values. (1p)
# 5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and
# subdirectories lab1, lab2 etc. (0.5p)
# Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.


# task 1
def f(x):
    return 2 * x ** 2 + 2 * x + 2


outputs = []
for x in range(56, 101):
    outputs += [f(x)]

print(outputs)


# task2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        output = 1
        for i in range(2, n+1):
            output *= i
    return output


number = int(input("Give me a number: "))
print("Factorial of your number is: ", factorial(number))


# task 3
import numpy as np


def the_lowest_in_array(array):
    index = 0
    min_val = None
    the_index = index
    for arr in array:
        for num in arr:
            if min_val is None:
                min_val = num
            elif num < min_val:
                min_val = num
                the_index = index
            index += 1
    return min_val, the_index


array = np.array([[7, 2, 5],
                  [5, 2, 10]])
print(array)
v, i = the_lowest_in_array(array)
print("The lowest value is", v, "and its index is", i)

