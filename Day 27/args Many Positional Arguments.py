"""
*args: Many Positional Arguments

In the last lesson,we looked at how to provide default values for optional arguments.
In this lesson, we'll discuss how to create functions that can take any number of arguments.

Let's say that we had a function called add,which adds n1 and n2 and it just returns the sum of those numbers.
What if I wanted to add more than two numbers?
what if I wanted to make this function more flexible and to allow any number of arguments to be used as the input?
Just simply change the code to use the asterix symbol and then the name of the parameter.

The asterix tells python that the function can accept any number of arguments
you can actually loop through all the arguments which is going to be in the form of a tuple
and do whatever it is you want with each of those arguments.
"""


def add(*args):
    print(type(args))
    print(args)  # A tuple of numbers
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    print(sum)


add(3, 5, 6, 2, 1, 7, 4, 3)
