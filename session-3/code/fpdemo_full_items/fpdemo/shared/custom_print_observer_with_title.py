
#chapter1
#observable_print_example_2.py
class CustomPrintObserverWithTitle():

    def __init__(self,title):
        self.title = title
    def on_next(self,data):
        print(self.title,"next",data)
    def on_completed(self):
        print(self.title , "Completed")
    def on_error(self,err):
        print(self.title , "Error",err)