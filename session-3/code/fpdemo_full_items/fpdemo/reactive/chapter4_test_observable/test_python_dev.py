from unittest import TestCase

from rx.testing import TestScheduler, ReactiveTest
from rx.testing.mockobserver import MockObserver

from reactive.chapter4_test_observable.python_dev import python_dev_in_chennai, python_dev_in_bangalore, \
    updatePythonDevInChennaiSalary


def values_in(mock_observer):
    return [item.value.value for item in mock_observer.messages]


def schedule_with(scheduler, subject, observer):
    def action(scheduler, state):
        subject.subscribe(observer)
    scheduler.schedule_absolute(1, action )


class Test(TestCase):
    def test_update_python_dev_in_chennai_salary(self):
        scheduler = TestScheduler()
        python_dev_in_chennai_values = scheduler.create_observer()
        python_dev_in_bangalore_values = scheduler.create_observer()

        schedule_with(scheduler, python_dev_in_chennai, python_dev_in_chennai_values)
        schedule_with(scheduler, python_dev_in_bangalore, python_dev_in_bangalore_values)

        scheduler.start()
        updatePythonDevInChennaiSalary(1200000)

        self.assertEqual(values_in(python_dev_in_chennai_values), [
            1000000,
            1200000
        ])

        self.assertEqual(values_in(python_dev_in_bangalore_values), [
            1260000,
            1512000
        ])

    def test_update_python_dev_old_in_chennai_salary_v0(self):
        scheduler = TestScheduler()
        python_dev_in_chennai_values = scheduler.create_observer()
        python_dev_in_bangalore_values = scheduler.create_observer()

        scheduler.schedule_absolute(0, action=lambda scheduler, state: python_dev_in_chennai.subscribe(
        python_dev_in_chennai_values))
        scheduler.schedule_absolute(0, action=lambda scheduler, state: python_dev_in_bangalore.subscribe(
        python_dev_in_bangalore_values))
        scheduler.start()
        updatePythonDevInChennaiSalary(1200000)

        self.assertEqual(values_in(python_dev_in_chennai_values), [
            1000000,
            1200000
        ])

        self.assertEqual(values_in(python_dev_in_bangalore_values), [
            1260000,
            1512000
        ])

    # self.assertEqual(python_dev_in_bangalore_values.messages, [
    #     ReactiveTest.on_next(10,1000000),
    #     ReactiveTest.on_next(20,1000000)
    # ])

    # assert results1.messages == [
    #     on_next(340, 5),
    #     on_next(410, 6),
    #     on_next(520, 7)]
    #
    # self.assertEqual(python_dev_in_chennai.value,1000000)
    # python_dev_in_bangalore_value = python_dev_in_bangalore.run()
    # self.assertEqual(python_dev_in_chennai.value,1000000)
    # self.assertEqual(python_dev_in_bangalore_value,1000000)
