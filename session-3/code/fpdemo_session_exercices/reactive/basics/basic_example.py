import rx
from rx.subject import BehaviorSubject
from rx import operators as ops

from shared.PrintObserver import PrintObserver



def calaculate_python_dev_salary():
    python_dev_in_chennai = BehaviorSubject(1000000)
    python_dev_in_bangalore = python_dev_in_chennai.pipe(
        ops.map(lambda value: value * (26/100))
        ops.subscribe_on()
    )


    python_dev_in_chennai.subscribe(
        on_next=lambda value:print("python_dev_in_chennai", value)
    )
    python_dev_in_bangalore.subscribe(
        on_next=lambda value:print("python_dev_in_bangalore", value)
    )

    python_dev_in_chennai.on_next(1200000)


def calaculate_python_dev_salary_imperative():
    python_dev_in_chennai = 1000000
    python_dev_in_bangalore = python_dev_in_chennai + (python_dev_in_chennai * (26/100))
    print("python_dev_in_bangalore", python_dev_in_bangalore)
    print("python_dev_in_chennai", python_dev_in_chennai)
    python_dev_in_chennai = 1200000
    print("python_dev_in_bangalore",python_dev_in_bangalore)
    print("python_dev_in_chennai",python_dev_in_chennai)



if __name__ == '__main__':
    calaculate_python_dev_salary()
    #calaculate_python_dev_salary_imperative()