import operator
from functools import reduce

def salary_from_user(user):
        return user['salary']

def salaries_for(users):
       return map(salary_from_user, users)

def user_of_gender(user,gender):
        return user['gender'] == gender

def users_of_gender(users,gender):
        user_by_gender = lambda user: user_of_gender(user,gender)
        return filter(user_by_gender,users)


def total_salaries_for_gender(users,gender):
        users_by_gender =  users_of_gender(users,gender)
        return reduce(operator.add, salaries_for(users_by_gender), 0)




def total_salaries_for_gender_v1(users,gender):
        return reduce(operator.add, map(lambda user: user['salary'],
                                        filter(lambda user: user['gender'] == gender, users)), 0)

def total_salaries_for_gender_v1(users,gender):
        users_of_gender =  filter(lambda user: user['gender'] == gender,users)
        return reduce (lambda accumulator,user: accumulator + user['salary'],users_of_gender,0)