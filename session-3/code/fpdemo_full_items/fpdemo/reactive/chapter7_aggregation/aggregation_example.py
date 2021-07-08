import rx

from shared.print_observer import PrintObserver
from shared.products import get_products
from rx import operators as ops

products = get_products()

#find_total_price_of_footwear_category[18448]next 163962.0
def find_total_price_of_footwear_category():
    return rx.from_(products).pipe(
        ops.filter(lambda product: product['category'] == 'Footwear'),
        ops.reduce(lambda accumulator, current: accumulator + current['price'], 0)

    )

#find_count_of_review_for_watch_category[21424]next 59
def find_count_of_review_for_watch_category():
    return rx.from_(products).pipe(
        ops.filter(lambda product: product['category'] == 'Watches'),
        ops.flat_map(lambda product: product['reviews']),
        ops.count()

    )

#find_highest_price_for_clothing_category[23480]next 5398.0
def find_highest_price_for_clothing_category():
    def product_price_comparer(first_product, next_product):
        if first_product['price'] > next_product['price']:
            return -1
        if first_product['price'] < next_product['price']:
            return 1

        return 0

    return rx.from_(products).pipe(
        ops.filter(lambda product: product['category'] == 'Clothing'),
        ops.map(lambda product:product['price']),
        ops.max()

    )

#find_lowest_dealPriced_product_v0[18500]next 99.0
def find_lowest_dealPriced_product_v0():


    return rx.from_(products).pipe(
        ops.map(lambda product:product['dealPrice']),
        ops.min()

    )

#find_lowest_dealPriced_product[16936]next {'productId': 19, 'name': 'Sicons Conditioning Conditoner Dog Shampoo', 'category': 'Pet Supplies', 'price': 110.0, 'dealPrice': 99.0, 'description': 'Specifications of Sicons Conditioning Conditoner Dog Shampoo (200 ml) General Pet Type Dog Brand Sicons Quantity 200 ml Model Number SH.DF-02 Type Conditioning Fragrance Conditoner Form Factor Gel In the Box Sales Package Shampoo Sicons Dog Fashion Conditioner Aloe Rinse', 'manufacturer': 'Sicons', 'availableItems': 25, 'overAllRating': 4.0, 'imageUrl': 'https://picsum.photos/400?image=19', 'reviews': [{'id': 35, 'user': {'id': 35, 'name': 'Wanda Fitzpatrick', 'gender': 'female', 'city': 'Mannekensvere', 'state': 'WV', 'zipcode': '758062', 'country': 'Nicaragua', 'dateofbirth': '1967-08-06 02:17', 'email': 'sit@ullamcorpervelit.org', 'phoneNumber': '973-5764'}, 'rating': 5, 'comment': 'Wonderful', 'created': '2021-04-11 11:14'}, {'id': 36, 'user': {'id': 36, 'name': 'Quinn Chaney', 'gender': 'female', 'city': 'Seongnam', 'state': 'Gyeonggi', 'zipcode': '6870', 'country': 'Iraq', 'dateofbirth': '1994-01-21 01:44', 'email': 'eu.ultrices.sit@habitantmorbitristique.co.uk', 'phoneNumber': '1-689-296-7112'}, 'rating': 1, 'comment': 'Very Bad', 'created': '2021-05-09 11:14'}, {'id': 37, 'user': {'id': 37, 'name': 'Amal Bernard', 'gender': 'male', 'city': 'Caxias do Sul', 'state': 'Rio Grande do Sul', 'zipcode': '4406', 'country': 'Grenada', 'dateofbirth': '1972-01-16 06:30', 'email': 'diam@ullamcorper.com', 'phoneNumber': '1-605-720-1345'}, 'rating': 2, 'comment': 'Bad', 'created': '2021-05-05 11:14'}]}
def find_lowest_dealPriced_product():

    #1. If first_product is less than next_product will return negative.
    #2. If first_product is greater than next_product will return positive.
    #3. If next_product is equal to first_product will return zero.

    def deal_pricing_comparer(first_product, next_product):
        if first_product['dealPrice'] < next_product['dealPrice']:
            return -1
        if first_product['dealPrice'] > next_product['dealPrice']:
            return 1

        return 0

    return rx.from_(products).pipe(
        ops.min(deal_pricing_comparer)

    )



if __name__ == '__main__':
    #find_total_price_of_footwear_category().subscribe(PrintObserver("find_total_price_of_footwear_category"))
    #find_count_of_review_for_watch_category().subscribe(PrintObserver("find_count_of_review_for_watch_category"))
    #find_highest_price_for_clothing_category().subscribe(PrintObserver("find_highest_price_for_clothing_category"))
    find_lowest_dealPriced_product_v0().subscribe(PrintObserver("find_lowest_dealPriced_product_v0"))
    find_lowest_dealPriced_product().subscribe(PrintObserver("find_lowest_dealPriced_product"))