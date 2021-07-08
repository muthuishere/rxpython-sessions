from rx.subject import BehaviorSubject
from rx import operators as ops

from shared.print_observer import PrintObserver


def calaculate_python_dev_salary():
    python_dev_in_chennai = BehaviorSubject(1000000)
    python_dev_in_bangalore = python_dev_in_chennai.pipe(
        ops.map(lambda value: value + (value * (26/100)))
    )
    python_dev_in_chennai.subscribe(PrintObserver("Python Dev In Chennai"))
    python_dev_in_bangalore.subscribe(PrintObserver("Python Dev In Bangalore"))
    python_dev_in_chennai.on_next(1200000)

#Refactor one by one
def calaculate_python_dev_salary_v0():
    python_dev_in_chennai = 1000000
    python_dev_in_bangalore = python_dev_in_chennai + (python_dev_in_chennai * (26/100))
    print("python_dev_in_bangalore", python_dev_in_bangalore)
    print("python_dev_in_chennai", python_dev_in_chennai)

    python_dev_in_chennai = 1200000
    print("python_dev_in_bangalore",python_dev_in_bangalore)
    print("python_dev_in_chennai",python_dev_in_chennai)



if __name__ == '__main__':
    calaculate_python_dev_salary()