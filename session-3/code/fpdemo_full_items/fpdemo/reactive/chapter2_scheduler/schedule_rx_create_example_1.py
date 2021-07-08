import threading

import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler

from shared.custom_print_observer_with_title import CustomPrintObserverWithTitle
from shared.custom_print_with_thread_name_observer_with_title import CustomPrintWithThreadNameObserverWithTitle
from shared.users import get_users
from shared.custom_print_observer import CustomPrintObserver



#Run 1
#1. create CustomPrintWithThreadNameObserverWithTitle to include thread id
#2. print thread on main

#RUn 2
#1 . Create ThreadPoolScheduler
#               thread_pool_scheduler = ThreadPoolScheduler(2)
#2 . Update Subscription for male & female user
#                   male_users.subscribe(create_observer('Male User'),scheduler=thread_pool_scheduler)
#                  female_users.subscribe(create_observer('Female User'),scheduler=thread_pool_scheduler)
#3 .  Update Create Source Method to run with Scheduler
#           scheduler.schedule(push_users)
#               def push_users():
#4. Verify parameter for schedule
#5. Explain how the classes has been organized
#               ThreadPoolScheduler extends NewThreadScheduler extends xxxx
#6. Get into New Thread Scheduler for verifying parameter for schedule
#               ScheduledAction should be of type
#               ScheduledAction consists of scheduler,state

#RUn 3
#7. state can be passed with string,first
#               Print the state ,
#                  print("State",state)
#               it should be none

#8. update a parameter
#              scheduler.schedule(push_users,[23,45])
#               should print State [23, 45]



thread_pool_scheduler = ThreadPoolScheduler(2)

def create_source(source, scheduler):


    def push_users(scheduler,state):
        for user in get_users():
            source.on_next(user)

        # raise Exception("unable to do anything")
        print("State",state)
        source.on_completed()

    scheduler.schedule(push_users,[23,45])

#before state    Run 2
def create_source_v1(source, scheduler):


    def push_users(scheduler,state):
        for user in get_users():
            source.on_next(user)

        # raise Exception("unable to do anything")
        print("State",state)
        source.on_completed()

    scheduler.schedule(push_users)

def create_source_v0(source, scheduler):
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


create_observer = CustomPrintWithThreadNameObserverWithTitle
# After Observer
def emit_users_of_only_male():

    male_users.subscribe(create_observer('Male User'),scheduler=thread_pool_scheduler)
    female_users.subscribe(create_observer('Female User'),scheduler=thread_pool_scheduler)



def emit_users_of_only_male_v0():

    male_users.subscribe(CustomPrintObserverWithTitle('Male User'))
    female_users.subscribe(CustomPrintObserverWithTitle('Female User'))


if __name__ == '__main__':
    print(threading.get_ident(),"Starting App")
    emit_users_of_only_male()
    print(threading.get_ident(), "Ending App")
