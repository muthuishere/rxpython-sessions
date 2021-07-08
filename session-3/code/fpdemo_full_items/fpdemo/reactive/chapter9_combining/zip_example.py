from time import sleep

from shared.print_observer import PrintObserver
from rx.subject import BehaviorSubject
from rx import operators as ops
theme = BehaviorSubject("Default")
language = BehaviorSubject("en-us")



def update_preferences(val):
    print(type(val))
    print(val)
    #call some api to update preferences

def test_change_theme():
    theme.pipe(
        ops.zip(language)
    ).subscribe(update_preferences)
    theme.on_next("Black")
    sleep(1)
    language.on_next("fs-in")





if __name__ == '__main__':
    test_change_theme()