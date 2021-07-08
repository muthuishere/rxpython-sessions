


from rx.subject import Subject, ReplaySubject, BehaviorSubject

from shared.PrintObserver import PrintObserver
from shared.products import get_products

products = get_products()
first_product = products[0]
another_product = products[1]
third_product = products[2]

# Subscribing to  news paper in a library defined by numbe
def print_products_v3():
    products_stream = BehaviorSubject(None)
    products_stream.subscribe(PrintObserver("BehaviorSubject Subject"))
    products_stream.on_next(first_product)
    products_stream.on_next(another_product)
    products_stream.on_next(third_product)
    print("Value " ,products_stream.value)


# Subscribing to  news paper in a library defined by numbe
def print_products():
    products_stream = ReplaySubject(2)
    products_stream.on_next(first_product)
    products_stream.on_next(another_product)
    products_stream.on_next(third_product)
    products_stream.subscribe(PrintObserver("Replay Subject"))

# Subscribing to daily news paper
def print_products_subject():
    products_stream = Subject()
    products_stream.subscribe(PrintObserver("Subject"))
    products_stream.on_next(first_product)
    products_stream.on_next(another_product)


if __name__ == '__main__':
    print_products()