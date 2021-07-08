import sys
import threading

import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler, NewThreadScheduler
import logging

from reactive.scheduler.PrintNamedObserver import PrintNamedObserver

from shared.users import get_users

thread_pool_scheduler = ThreadPoolScheduler(2)


def create_source(source, scheduler):
    def action(scheduler, state):
        print("create_source", threading.get_ident())
        print("scheduler", scheduler)
        print("state", state)
        for user in get_users():
            source.on_next(user)
        source.on_completed()


    scheduler.schedule(action)

    # To Pass State , One Variable for schedule
    # return scheduler.schedule(action ,"Hi")


def emit_users_of_only_male():
    print_observer = PrintNamedObserver("Users of Male")
    users = rx.create(create_source)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(print_observer, scheduler=thread_pool_scheduler)


def create_source_without_scheduler(source, scheduler):
    for user in get_users():
        source.on_next(user)

    print("create_source", threading.get_ident())

    print("scheduler", scheduler)
    source.on_completed()


def emit_users_of_only_male_v1_print_observer():
    print_observer = PrintNamedObserver("Users of Male")
    users = rx.create(create_source_without_scheduler)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(print_observer)


def emit_users_of_only_male_v0():
    users = rx.create(create_source_without_scheduler)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(print)


if __name__ == '__main__':
    print(threading.get_ident(), "Start")
    emit_users_of_only_male()
    print(threading.get_ident(), "emit_users_of_only_male completed")
