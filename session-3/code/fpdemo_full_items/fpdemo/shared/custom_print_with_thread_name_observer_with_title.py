
#chapter1
#observable_print_example_2.py
import threading


class CustomPrintWithThreadNameObserverWithTitle():

    def __init__(self,title):
        self.title = title
    def get_prefix(self):
        return self.title + '[' + str(threading.get_ident()) + ']'
    def on_next(self,data):
        print(self.get_prefix() + "next", data)
    def on_completed(self):
        print(self.get_prefix() +  "Completed")
    def on_error(self,err):
        print(self.get_prefix() +  "Error",err)