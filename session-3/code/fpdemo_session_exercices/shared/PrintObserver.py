import threading


class PrintObserver():
    def __init__(self, title=""):
        self.suffix = '[' + title + '] '

    def on_next(self, data):
        print(threading.get_ident(), self.suffix + "Data received", data)

    def on_completed(self):
        print(threading.get_ident(), self.suffix + "Completed")

    def on_error(self, err):
        print(threading.get_ident(), self.suffix + "Error", err)
