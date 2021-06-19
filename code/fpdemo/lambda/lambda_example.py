square = lambda input: input * input
two_a_b = lambda a, b: 2 * a * b
squares_of = lambda a, b: square(a) + square(b)
a_plus_b_whole_square = lambda a, b: squares_of(a, b) + two_a_b(a, b)
a_minus_b_whole_square = lambda a, b: squares_of(a, b) - two_a_b(a, b)
