

import rx
from rx import  operators as ops

from shared.users import get_users


def create_source(source, scheduler):
    for user in get_users():
         source.on_next(user)

    source.on_completed()

def emit_all_salaries():
    observable = rx.create(create_source)
    observable.subscribe(print)


def emit_users_of_only_male():
    users = rx.create(create_source)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(print)


if __name__ == '__main__':
    emit_users_of_only_male()