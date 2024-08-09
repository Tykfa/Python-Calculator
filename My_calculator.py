class MyCalculator:
    """
    Calculator class that handles basic arithmetic operations.

    Attributes:
        current_value (float): Holds current result of calculations.
    """

    def __init__(self, starting_value: float = 0):
        """
        Initializes the calculator with a value.

        :param starting_value: The initial value for calculations, default is 0 unless specified diffrently.
        """
        self.current_value = starting_value

    def add(self, value_to_add: float):
        """
        Adds number to the current value.

        :param value_to_add: Value to be added to the current value.
        :return: updated current value after operation.
        """
        self.current_value += value_to_add
        return self.current_value

    def subtract(self, value_to_subtract: float):
        """
        Subtracts number from the current value.

        :param value_to_subtract: The value to be subtracted from the current value.
        :return: The updated current value after operation.
        """
        self.current_value -= value_to_subtract
        return self.current_value

    def multiply(self, multiplicator: float):
        """
        Multiplies current value by a given number.

        :param multiplicator: The value to multiply the current value by.
        :return: The updated current value after multiplying.
        """
        self.current_value *= multiplicator
        return self.current_value

    def divide(self, divider: float):
        """
         Raises an error if division by zero is attempted.
         Otherwise divides the current value by a given divider.

        :param divider: The value to divide the current value by.
        :return: The updated current value after division.
        :raises Exception: If division by zero is attempted.
        """
        if divider == 0:
            raise Exception("Sorry, division by zero is not possible. Operation canceled, value not changed")
        elif divider != 0:
            self.current_value /= divider
            return self.current_value
        else:
            pass

    def get_current_value(self):
        """
        Returns the current value.

        :return: The current value.
        """
        return self.current_value

    def reset_calculations(self):
        """
        Resets the calculator's current value to zero.

        :return: The updated current that equals 0.
        """
        self.current_value = 0
        return self.current_value
