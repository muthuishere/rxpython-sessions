import rx
from rx.scheduler import NewThreadScheduler, ThreadPoolScheduler
from rx import operators as ops
from shared.PrintObserver import PrintObserver
from shared.users import retrieve_all_users


new_thread_scheduler = NewThreadScheduler()
thread_pool_scheduler = ThreadPoolScheduler(2)

def from_demo():
    rx_from_observer = PrintObserver("Rx From Example")
    rx.from_(retrieve_all_users()).pipe(
        ops.subscribe_on(thread_pool_scheduler)
    ).subscribe(rx_from_observer)

def just_demo():
    rx_just_observer = PrintObserver("Rx Just Example")
    rx.just(retrieve_all_users()).subscribe(rx_just_observer, scheduler=new_thread_scheduler)



if __name__ == '__main__':
    print("Starting App")
    from_demo()
    just_demo()
    print("Ending App")


