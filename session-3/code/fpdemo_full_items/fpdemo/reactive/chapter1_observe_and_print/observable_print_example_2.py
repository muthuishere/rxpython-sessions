import rx
from rx import operators as ops

from shared.custom_print_observer_with_title import CustomPrintObserverWithTitle
from shared.users import get_users
from shared.custom_print_observer import CustomPrintObserver


def create_source(source, scheduler):
    for user in get_users():
        source.on_next(user)

    # raise Exception("unable to do anything")
    source.on_completed()


users = rx.create(create_source)



def filter_users_by_gender(gender):
    return ops.filter(lambda user: user['gender'] == gender)


fetch_users_by_gender = lambda gender: users.pipe(filter_users_by_gender(gender))

male_users = fetch_users_by_gender('Male')
female_users = fetch_users_by_gender('Female')


# After Observer
def emit_users_of_only_male():

    male_users.subscribe(CustomPrintObserverWithTitle('Male User'))
    female_users.subscribe(CustomPrintObserverWithTitle('Female User'))

#
# def emit_users_of_only_male_v0():
#     male_users.subscribe(print_observer)
#     female_users.subscribe(print_observer)


if __name__ == '__main__':
    emit_users_of_only_male()
