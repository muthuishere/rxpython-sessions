import threading

import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler

from shared.PrintObserver import PrintObserver
from shared.users import retrieve_all_users

thread_pool_scheduler = ThreadPoolScheduler(2)




users = rx.from_(retrieve_all_users())


def fetch_users_by_gender(gender):
    return users.pipe(
        ops.filter(lambda user: user['gender'] == gender)
    )


def emit_users_based_on_gender():
    male_users = fetch_users_by_gender('Male')
    female_users = fetch_users_by_gender('Female')
    print(threading.get_ident(), "Printing Male Users")
    print_observer_for_male = PrintObserver("male_users")
    male_users.subscribe(print_observer_for_male, scheduler=thread_pool_scheduler)
    print(threading.get_ident(), "Printing Female Users")
    female_users.subscribe(PrintObserver("female_users"),scheduler=thread_pool_scheduler)


if __name__ == '__main__':
    print(threading.get_ident(), "Starting App")
    emit_users_based_on_gender()
    print(threading.get_ident(), "Ending App")
