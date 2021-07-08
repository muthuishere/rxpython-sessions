from datetime import timedelta

import rx
from rx import operators as ops

from shared.print_observer import PrintObserver
from shared.products import get_invalid_products, get_products

import requests


def get_product_urls_from_server(product_id):
    response = requests.get(f"http://localhost:1420/producturls/{product_id}")
    return response.json()


def get_product_urls_from_cache(product_id):
    print("getting cached version")
    return {
        "id": f"{product_id}",
        "urls": [
            f"https://www.bit.ly/products/{product_id}"

        ]
    }

#Give back the cached version after 3 times
def get_product_urls_for(product):
    return rx.just(product).pipe(
        ops.map(lambda product: product['productId']),
        ops.map(lambda productId: get_product_urls_from_server(productId)),
        ops.retry(3),
        ops.catch(rx.just(get_product_urls_from_cache(product['productId'])))


    )

#Stop the server and go for retry
def get_product_urls_for_v1(product):
    return rx.just(product).pipe(
        ops.map(lambda product: product['productId']),
        ops.map(lambda productId: get_product_urls_from_server(productId)),
        ops.retry(3)

    )


#Stop the server
def get_product_urls_for_v0(product):
    return rx.just(product).pipe(
        ops.map(lambda product: product['productId']),
        ops.map(lambda productId: get_product_urls_from_server(productId))
    )


if __name__ == '__main__':
    first_product = get_products()[1]
    get_product_urls_for(first_product).subscribe(PrintObserver("list_product_buy_urls"))
