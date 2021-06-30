from functools import partial


def add_two_numbers_and_multiply_third(x,y,z):
    return (x+y) * z

add_two_numbers = partial(add_two_numbers_and_multiply_third, z = 1)
increment_one = partial(add_two_numbers_and_multiply_third, y=1,z = 1)

multiply_two_numbers = partial(add_two_numbers_and_multiply_third, x = 0)