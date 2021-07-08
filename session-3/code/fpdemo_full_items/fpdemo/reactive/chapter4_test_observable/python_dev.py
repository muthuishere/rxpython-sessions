from rx.subject import BehaviorSubject
from rx import operators as ops

from shared.print_observer import PrintObserver

python_dev_in_chennai = BehaviorSubject(1000000)
python_dev_in_bangalore = python_dev_in_chennai.pipe(
    ops.map(lambda value: value + (value * (26 / 100)))
)


def updatePythonDevInChennaiSalary(salary):
    python_dev_in_chennai.on_next(salary)
