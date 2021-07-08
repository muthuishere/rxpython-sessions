import rx

from shared.print_observer import PrintObserver
from shared.products import get_products
from rx import operators as ops

products = get_products()

def filter_only_footwear():
    return rx.from_(products).pipe(
        ops.filter(lambda product:product['category'] == 'Footwear')
    )

def filter_footwear_and_take_3_elements():
    return filter_only_footwear().pipe(
        ops.take(3),
    )

def list_users_with_in_review_flatmap():
    return rx.from_(products).pipe(
        ops.flat_map(lambda product:product['reviews']),
        ops.map(lambda review:review['user'])
    )
def list_users_with_in_review_distinct():
    return rx.from_(products).pipe(
        ops.flat_map(lambda product:product['reviews']),
        ops.map(lambda review:review['user']),
        ops.distinct()
    )

def filter_footwear_and_take_3_elements_v0():
    return rx.from_(products).pipe(
        ops.filter(lambda product:product['category'] == 'Footwear'),
        ops.take(3),
    )


if __name__ == '__main__':
    #filter_only_footwear().subscribe(PrintObserver("Filter Only Footwear"))
    #filter_footwear_and_take_3_elements().subscribe(PrintObserver("Filter Only Footwear with first 10 elements"))
    #list_users_with_in_review_flatmap().subscribe(PrintObserver("list_users_with_in_review_flatmap"))
    list_users_with_in_review_distinct().subscribe(PrintObserver("list_users_with_in_review_distinct"))