import threading


class PrintNamedObserver():
    def __init__(self, title):
        self.title = title

    def on_next(self, value):
        print(threading.get_ident(), "[", self.title, "]", value)

    def on_error(self, exception):
        print(threading.get_ident(), "[", self.title, "]", "error", exception)

    def on_completed(self):
        print(threading.get_ident(), "on_completed")
