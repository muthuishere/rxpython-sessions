import rx
from rx.subject import Subject,ReplaySubject,BehaviorSubject,AsyncSubject

#the rx.create ,you cannot place data whenever you want
#that same applicable for just from
# if you need a place which supports something like Baggage carousel Subject is where you should go
# we will see that in detail later,
#But before we see ,how subject can be utilized

#RUn 1 - Subject
# create two
        #products = get_products()
        # first_product = products[0]
        # second_product = products[1]
#Create method print_products
    # from rx.subject import Subject,

    # product_stream = Subject()
    # product_stream.subscribe(PrintObserver())
    # product_stream.on_next(first_product)
  # Note value is printed , as   subscribe is called before on Next

#Run 2 - Subject
    # Modify
        # product_stream = Subject()
        # product_stream.on_next(first_product)
        # product_stream.subscribe(PrintObserver())
    # Note value is not printed , as   subscribe is called after on Next
    #How to send messages though set on next


#Run 3 - Replay subject
    # A subject with bufferable , All elements will be emitted regardless of observer , when they have values in buffer
        # product_stream = ReplaySubject(2)
        # product_stream.on_next(first_product)
        # product_stream.on_next(second_product)
        # product_stream.subscribe(PrintObserver())
       # How to get the latest value or how to examine


#Run 4 - Behavior subject
    # similar like Replay Subject, But only one Buffer also it has away to check the current value
            # product_stream = BehaviorSubject(None)
            # product_stream.on_next(first_product)
            # product_stream.on_next(second_product)
            # product_stream.subscribe(PrintObserver())
            # print("current product", product_stream.value)
                # Why Completed not emitted
                # Why not Emitted
                # Baggage corrosel will keep on running , which is a memory leak
                # EIther there should be a dispose or should be completed

                # a stream is terminated ( onComplete / onError has been called ),
                # subscriber unsubscribes automatically.
                # You should be able to test these behaviors using isUnsubscribed() method on the Subscription object.


#Run 5 - Behavior subject
        # product_stream = BehaviorSubject(None)
        # product_stream.subscribe(PrintObserver())
        # product_stream.on_next(first_product)
        # product_stream.on_next(second_product)
        # print("current product", product_stream.value)
        # product_stream.on_completed()

#Run 6 - AsyncSubject
    # #Async subject emits only after completed
    #
    # product_stream = AsyncSubject()
    # product_stream.subscribe(PrintObserver())
    # product_stream.on_next(first_product)
    # product_stream.on_next(second_product)
    # product_stream.on_completed()
    #
    # #Async subject emits only one value after completed

    
from shared.print_observer import PrintObserver
from shared.products import get_products

products = get_products()
first_product = products[0]
second_product = products[1]


def print_products():
    product_stream = AsyncSubject()
    product_stream.subscribe(PrintObserver())
    product_stream.on_next(first_product)
    product_stream.on_next(second_product)
    print("current product", product_stream.value)
    product_stream.on_completed()


    #Why not Emitted

#Async subject emits only latest value after completed
def print_products():
    product_stream = AsyncSubject()
    product_stream.subscribe(PrintObserver())
    product_stream.on_next(first_product)
    product_stream.on_next(second_product)
    product_stream.on_completed()


#Async subject emits only after completed
def print_products():
    product_stream = AsyncSubject()
    product_stream.subscribe(PrintObserver())
    product_stream.on_next(first_product)
    product_stream.on_completed()

def print_products_v5():
    product_stream = AsyncSubject()
    product_stream.subscribe(PrintObserver())
    product_stream.on_next(second_product)






def print_products_v4():
    product_stream = BehaviorSubject(None)
    product_stream.subscribe(PrintObserver())
    product_stream.on_next(first_product)
    product_stream.on_next(second_product)
    print("current product", product_stream.value)
    product_stream.on_completed()
    #Why Completed not emitted
    #Why not Emitted
    # Baggage corrosel will keep on running , which is a memory leak
        #EIther there should be a dispose or should be completed

    #a stream is terminated ( onComplete / onError has been called ),
    # subscriber unsubscribes automatically.
    # You should be able to test these behaviors using isUnsubscribed() method on the Subscription object.

def print_products_v4():
    product_stream = BehaviorSubject(None)
    product_stream.on_next(first_product)
    product_stream.on_next(second_product)
    product_stream.subscribe(PrintObserver())
    print("current product", product_stream.value)
    #Why Completed not emitted

def print_products_v3():
    product_stream = ReplaySubject()
    product_stream.on_next(first_product)
    product_stream.on_next(second_product)
    product_stream.subscribe(PrintObserver())
    print("current product", product_stream.value)
    #What is the current product product Stream holds

def print_products_v2():
    product_stream = Subject()
    product_stream.on_next(first_product)
    product_stream.subscribe(PrintObserver())
    product_stream.on_next(second_product)

def print_products_v1():
    product_stream = Subject()
    product_stream.on_next(first_product)
    product_stream.subscribe(PrintObserver())

def print_products_v0():
    product_stream = Subject()
    product_stream.subscribe(PrintObserver())
    product_stream.on_next(first_product)


if __name__ == '__main__':
    print("Start")
    print_products_v1()
    print("Completed")



