import rx
from rx import operators as ops
from shared.users import get_users
from shared.custom_print_observer import CustomPrintObserver


def create_source(source, scheduler):
    for user in get_users():
        source.on_next(user)

    #raise Exception("unable to do anything")
    source.on_completed()


users = rx.create(create_source)
print_observer = CustomPrintObserver()


def filter_users_by_gender(gender):
    return ops.filter(lambda user: user['gender'] == gender)


fetch_users_by_gender = lambda gender: users.pipe(filter_users_by_gender(gender))

male_users = fetch_users_by_gender('Male')
female_users = fetch_users_by_gender('Female')


#
# def filter_users_by_gender(gender):
#     return ops.filter(lambda user: user['gender'] == gender)
#
# male_users = users.pipe(filter_users_by_gender('Male'))
# female_users = users.pipe(filter_users_by_gender('Female'))


#
# filter_users_by_gender = lambda gender:ops.filter(lambda user: user['gender'] == gender)
# male_users = users.pipe(filter_users_by_gender('Male'))
# female_users = users.pipe(filter_users_by_gender('Female'))

#
# filter_male_users = ops.filter(lambda user: user['gender'] == 'Male')
# filter_female_users = ops.filter(lambda user: user['gender'] == 'Female')
# male_users = users.pipe(filter_male_users)
# female_users = users.pipe(filter_female_users)

# Start with
# male_users = users.pipe(
#     ops.filter(lambda user: user['gender'] == 'Male')
# )

# After Observer
def emit_users_of_only_male():
    male_users.subscribe(print_observer)
    female_users.subscribe(print_observer)


# After Observer
def emit_users_of_only_male_v2():
    users = rx.create(create_source)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    observer = CustomPrintObserver()
    male_users.subscribe(observer)


# Start WIth
def emit_users_of_only_male_v1():
    users = rx.create(create_source)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(
        on_next=lambda data:print('next',data),
        on_completed=lambda :print('completed'),
        on_error=lambda err :print('error',err),
    )


# Start WIth
def emit_users_of_only_male_v0():
    users = rx.create(create_source)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(print)


if __name__ == '__main__':
    emit_users_of_only_male()

