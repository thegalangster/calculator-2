"""Functions for common math operations."""
from functools import reduce

def add(num_array):
    """Return the sum of the two inputs."""
    return reduce(lambda x, y: x+y, num_array)

def subtract(num_array):
    """Return the second number subtracted from the first."""
    return reduce(lambda x, y: x-y, num_array)

def multiply(num_array):
    """Multiply the two inputs together."""
    return reduce(lambda x, y: x*y, num_array)

def divide(num_array):
    """Divide the first input by the second and return the result."""
    return reduce(lambda x, y: x/y, num_array)


def square(num1):
    """Return the square of the input."""
    return num1*num1

def cube(num1):
    """Return the cube of the input."""
    return num1*num1*num1

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1**num2

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return num1%num2

def add_mult(num1, num2, num3):
    """ Takes three numbers, adds the first two, then multiplies the sum with the third """
    sum1 = num1 + num2
    return sum1 * num3

def add_cubes(num1, num2):
    """ Takes two numbers, and adds together the cubes of those numbers """
    cube1 = num1 * num1 * num1
    cube2 = num2 * num2 * num2
    return cube1 + cube2

