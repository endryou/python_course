from python_course_mm.lab3_f_1 import count_field
import sys


def compare_two_figs(fig1, fig2):
    if fig1 == None or fig2 == None:
        sys.exit("Lack of argument, cannot compare figures")
    if len(fig1) > 3 or len(fig2) > 3:
        sys.exit("Too many arguments, Program stops")
    fig1_name, fig1_field = count_field(*fig1)
    fig2_name, fig2_field = count_field(*fig2)
    if fig1_field > fig2_field:
        return print(f"The first figure ({fig1_name}) has larger field")
    else:
        return print(f"The second figure ({fig2_name}) has larger field")


figure_one = ('Circle', 5)
figure_two = ('rhOMBus', 5, 0.000000000000000003)
compare_two_figs(figure_one, figure_two)

