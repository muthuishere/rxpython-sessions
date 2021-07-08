import threading
import time

import rx

from shared.products import get_products


def products_with_just():
    return rx.just(get_products())

def products_with_from_():
    return rx.from_(get_products())

#Start With Thread
def print_all_products_each_after_two_seconds():
    for product in get_products():
        time.sleep(1)
        print(product)


if __name__ == '__main__':
        print("Start")
        thread = threading.Thread(target=print_all_products_each_after_two_seconds)
        thread.run()
        print("End")

#
# if __name__ == '__main__':
#         print("Start")
#         thread = threading.Thread(target=print_all_products_each_after_two_seconds)
#         thread.start()
#         print("End")
#         thread.join()