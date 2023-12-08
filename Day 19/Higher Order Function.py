"""
# Function as Inputs

def function_a(something):
    # Do this with something
    # Then do this
    # Finally do this

def function_b():
    # Do this

function_a(function_b)
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2


"""
The idea of a higher order function is a function that can work with other functions

The calculator is a higher order function, taking another function as an input then work
it inside the body of the function
"""
def calculator(n1, n2, func):

    return func(n1, n2)

result = calculator(5,2, multiply)
print(result)


