
from functools import reduce


def salary_accumulator(accumulator, user):
    return accumulator + user['salary']

def total_salaries_for(users):
    return reduce(salary_accumulator, users, 0)


def total_salaries_for_imperative(users):
    result = 0
    for user in users:
        result += user['salary']
    return result
