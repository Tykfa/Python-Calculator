import pytest
from My_calculator import MyCalculator


@pytest.fixture
def my_calculator() -> MyCalculator:
    """
    Create MyCalculator instance.

    :return: MyCalculator instance.
    """
    return MyCalculator()


def test_add(my_calculator):
    my_calculator.add(5)
    assert my_calculator.get_current_value() == 5


def test_subtract(my_calculator):
    my_calculator.subtract(3)
    assert my_calculator.get_current_value() == -3


def test_multiply(my_calculator):
    my_calculator.add(2)
    my_calculator.multiply(3)
    assert my_calculator.get_current_value() == 6


def test_divide(my_calculator):
    my_calculator.add(10)
    my_calculator.divide(2)
    assert my_calculator.get_current_value() == 5


def test_divide_by_zero(my_calculator):
    with pytest.raises(Exception,
                       match="Sorry, division by zero is not possible. Operation canceled, value not changed"):
        my_calculator.divide(0)


def test_reset_calculations(my_calculator):
    my_calculator.add(10)
    my_calculator.reset_calculations()
    assert my_calculator.get_current_value() == 0


def test_chaining_operations(my_calculator):
    my_calculator.add(10)
    my_calculator.subtract(2)
    my_calculator.multiply(3)
    my_calculator.divide(4)
    assert my_calculator.get_current_value() == 6


def test_floating_point_operations(my_calculator):
    my_calculator.add(0.5)
    my_calculator.multiply(2.3)
    assert my_calculator.get_current_value() == 1.15


@pytest.mark.parametrize("initial, operations, expected", [
    (0, [("add", 10), ("subtract", 2), ("multiply", 3), ("divide", 2)], 12),
    (5, [("multiply", 2), ("subtract", 1), ("divide", 2)], 4.5),
    (10, [("divide", 2), ("add", 3), ("multiply", 2)], 16),
])
def test_parametrized_operations(initial, operations, expected):
    my_calculator = MyCalculator(initial)
    for op, value in operations:
        getattr(my_calculator, op)(value)
    assert my_calculator.get_current_value() == expected
