import asyncio
import sys
import threading
from asyncio import wait

import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler, NewThreadScheduler
import logging

from rx.scheduler.eventloop import AsyncIOScheduler

from reactive.scheduler.PrintNamedObserver import PrintNamedObserver

from shared.users import get_users

thread_pool_scheduler = ThreadPoolScheduler(2)



async def wait_until():
    await asyncio.sleep(3)
    return True


#from_list example with Async IO Scheduler

# The event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.
#
# Application developers should typically use the high-level asyncio functions, such
# as asyncio.run(), and should rarely need to reference the loop object or call its methods. This section is intended mostly
# for authors of lower-level code, libraries, and frameworks, who need finer control over the event loop behavior.
def emit_users_of_only_male():
    print_observer = PrintNamedObserver("Users of Male async_io_scheduler new_event_loop")
    #loop = asyncio.new_event_loop()
    loop = asyncio.get_event_loop()


    async_io_scheduler = AsyncIOScheduler(loop)
    users = rx.from_list(get_users(),scheduler=async_io_scheduler)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(print_observer)




    loop.run_until_complete(wait_until())





def emit_users_of_only_male_old_event_loop():
    print_observer = PrintNamedObserver("Users of Male async_io_scheduler get event loop")
    loop = asyncio.get_event_loop()
    async_io_scheduler = AsyncIOScheduler(loop)
    users = rx.from_list(get_users(),scheduler=async_io_scheduler)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(print_observer)
    loop.run_forever()
    loop.close()



#from_list example with thread pool scheduler on top
def emit_users_of_only_male_v1():
    print_observer = PrintNamedObserver("Users of Male thread_pool_scheduler")
    users = rx.from_list(get_users(),scheduler=thread_pool_scheduler)
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(print_observer)

#from_list example with thread pool scheduler
def emit_users_of_only_male_v0():
    print_observer = PrintNamedObserver("Users of Male")
    users = rx.from_list(get_users())
    male_users = users.pipe(
        ops.filter(lambda user: user['gender'] == 'Male')
    )
    male_users.subscribe(print_observer, scheduler=thread_pool_scheduler)



if __name__ == '__main__':
    print(threading.get_ident(), "Start")
    emit_users_of_only_male()
    #emit_users_of_only_male_v0()
    print(threading.get_ident(), "emit_users_of_only_male completed")
