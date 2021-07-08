

import rx
from rx import  operators as ops

from shared.PrintObserver import PrintObserver
from shared.users import retrieve_all_users


def create_source(pipeline, scheduler):
    for user in retrieve_all_users():
         pipeline.on_next(user)
    pipeline.on_completed()




def emit_all_salaries():
    observable = rx.create(create_source)
    observable.subscribe(print)


users = rx.create(create_source)

def fetch_users_by_gender(gender):
    return users.pipe(
        ops.filter(lambda user: user['gender'] == gender)
    )

def emit_users_of_only_male():
    male_users = fetch_users_by_gender('Male')
    male_users.subscribe(PrintObserver("male_users"))



def emit_users_based_on_gender():
    male_users = fetch_users_by_gender('Male')
    female_users = fetch_users_by_gender('Female')
    print("Printing Male Users")
    male_users.subscribe(PrintObserver("male_users"))
    print("Printing Female Users")
    female_users.subscribe(PrintObserver("female_users"))



if __name__ == '__main__':
    print("Starting App")
    emit_users_based_on_gender()
    print("Ending App")