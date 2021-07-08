import threading

import rx
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler, NewThreadScheduler

from shared.custom_print_observer_with_title import CustomPrintObserverWithTitle
from shared.custom_print_with_thread_name_observer_with_title import CustomPrintWithThreadNameObserverWithTitle
from shared.products import get_products

#thread_pool_scheduler = ThreadPoolScheduler(2)
new_thread_scheduler = NewThreadScheduler()

def products_with_just():
    return rx.just(get_products())

def products_with_from_():
    return rx.from_(get_products())

#Run 1
# Create products_with_just
#           rx.just(get_products())
# in main function
#       print(threading.get_ident(),"Starting")
#       products_with_just().subscribe(CustomPrintWithThreadNameObserverWithTitle('products_with_just'))

#Run 2
# Create products_with_from_
#   rx.from_(get_products())
# in main function
#       products_with_from_().subscribe(CustomPrintWithThreadNameObserverWithTitle('products_with_from_'))


#Run 3
# On SUbscribe new_thread_scheduler
# new_thread_scheduler = NewThreadScheduler()
# in main function
#        products_with_just().subscribe(CustomPrintWithThreadNameObserverWithTitle('products_with_just'), scheduler=new_thread_scheduler)


if __name__ == '__main__':
    print(threading.get_ident(),"Starting")
    products_with_just().subscribe(CustomPrintWithThreadNameObserverWithTitle('products_with_just'), scheduler=new_thread_scheduler)
    #products_with_from_().subscribe(CustomPrintWithThreadNameObserverWithTitle('products_with_from_'))
    print(threading.get_ident(), "Completed")
