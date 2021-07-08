import threading

from rx.core.typing import Observer


class PrintObserver(Observer):
    # def __init__(self):
        # self._on_next = on_next
        # self._on_error = on_error
        # self._on_completed = on_completed

    def on_next(self, value):
        print(threading.get_ident(), value)


    def on_error(self, exception):
        print(threading.get_ident(),"error", exception)

    def on_completed(self):
        print(threading.get_ident(),"on_completed")