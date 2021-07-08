
#chapter1
#observable_print_example_1.py
class CustomPrintObserver():
    def on_next(self,data):
        print("next",data)
    def on_completed(self):
        print("Completed")
    def on_error(self,err):
        print("Error",err)