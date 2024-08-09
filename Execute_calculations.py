from My_calculator import MyCalculator


def main():
    """
    Function to visualise the usage of the MyCalculator class in terminal.

    This function creates an instance of MyCalculator, performs a combination of
    arithmetic operations, and prints the results after each operation. Finally, it gets and prints the
    final value that the calculator got.
    """
    mc = MyCalculator()
    print(mc.add(10))  # Adds 10 to the current value (0) and prints the result
    print(mc.subtract(2))  # Subtracts 2 from the current value (10) and prints the result
    print(mc.multiply(4))  # Multiplies the current value (8) by 4 and prints the result
    print(mc.divide(9))  # Divides the current value (32) by 9 and prints the result
    final_value = mc.get_current_value()
    print(final_value)  # Prints the final value of the calculator


if __name__ == "__main__":
    main()
