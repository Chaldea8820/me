# -*- coding: UTF-8 -*-
"""Set 3, Exercise 1.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Using a while loop make a list of numbers that goes from the start number up
    to, but not including, the stop number, in increments of step. E.g.:
        start: 3
        stop: 10
        step: 2
        will return: [3, 5, 7, 9]
    Look up for how range() works in the python docs. You could  answer this
    with just the range function, but we'd like you to do it the long way.
    """
    list_1 = []
    for i in range (start, stop,step)
        list_1.append(i)
        return list_1





def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2

    You can either reuse loop_ranger, or the range function that in the standard library
    """
    list_2 = []
    for i in range (start, stop, 2)
        list_2.append(i)
        return list_2


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for a function called "input"
    """
    message = f"Give me a number between {low} and {high}: "
    
    while True:
        try:
            input_num = int(input(message))
            if low < input_num < high:
                print(f"{input_num} Passes")
                return input_num
            else:
                print(f"{input_num} Fails")
                except ValueError:
            print("number dumbass")

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    message = "Give me a number: "
    print(message)
    
    while True:
        try:
            input_num = int(input(message))
            print("{} Passes".format(input_num))
            return input_num
        
        except Exception as e:
            print("Number fuckwit")  


def super_asker(low, high):
    message = "number between {} and {}: ".format(low, high)
    
    while True:
        try:
            input_num = int(input) 
            
            if low < input_num < high:
                print("{} Passes".format(input_num))
                return input_num 
            else:
                print("{} Fails".format(input_num, low, high))
        
        except Exception as e:
            print("Number fuckwit.")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
