from typing import Callable, Union

"""defensive programming calculator program, with detailed docstrings and type annotating"""


# define functions
def add(n1: int, n2: int) -> int:
    """Adds n1 and n2 and returns the results

    Args: n1 - first int to add
          n2 - second int to add"""
    return n1 + n2


def minus(n1: int, n2: int) -> int:
    """Subtracts n1 from n2 and returns the results

        Args: n1 - int to subtract from
              n2 - int value to be subtracted from n1"""
    return n1 - n2


def multiply(n1: int, n2: int) -> int:
    """Multiplies n1 and n2 and returns the results

        Args: n1 - first int to be multiplied
              n2 - second int to be multiplied"""
    return n1 * n2


def divide(n1: int, n2: int) -> float:
    """Divides n1 by n2 and returns the results

        Args: n1 - int to be numerator
              n2 - int to be denominator """
    return n1 / n2


def calculator(operation: Callable, n1: int, n2: int) -> Union[float, int]:  # type annotating
    """Takes in 3 args, a function and 2 integers and returns the function passing in the two integers as arguments

            Args: n1 - int to be arg1 in operation function
                  n2 - int to be arg2 in operation function
                  operation - a callable function with 2 arg inputs"""
    return operation(n1, n2)


def run_calculator() -> str:
    """Asks user for 2 inputs and tries to make each an integer, then asks user to input an operation and tries to use
     that input as a key to call the operation and input two numbers as arguments. Returns the result if no errors."""

    try:
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
    except ValueError as error:
        print(f"{error} is not a number, please enter a number")
        return run_calculator()
    else:
        operation = input("Would you like to multiply, divide, add or subtract the first number from the second? ")

        try:
            print(calculator(operations_dict[operation][0], num1, num2))
            result = f"{num1} {operations_dict[operation][1]} {num2} = " \
                     f"{calculator(operations_dict[operation][0], num1, num2)}"

        except KeyError:
            print("This operation does not exist, try again")
            return run_calculator()
        except ZeroDivisionError:
            print("You cannot divide by zero, try again")
            return run_calculator()

        else:
            print(result)
            return result


def readfile() -> None:
    """Asks user to input filename, tries to read file, if file does not exist, throws an error and recursively asks
    until it does exist. If file read, it prints out file contents."""
    try:
        with open(f"{input('Enter file name ')}.txt", "r") as eqn_file:
            data = eqn_file.readlines()
    except FileNotFoundError:
        print("Could not find file, please try again")
        readfile()
    else:
        for line in data:
            print(line)


def option_decision() -> None:
    # ask user to either view eqns or enter one
    choice = input(" Do you want to view equations from txt file (type 0) or add a calculation? (type 1) ")

    if choice == "1":
        # run calculator and write output into eqn file
        another_equation = True
        while another_equation:
            eqn = run_calculator()
            cont = input("if you would like to add another equation, press any button, if you would like to exit the "
                         "code, enter 'e': ")
            if cont == "e":
                another_equation = False

            with open("equations.txt", "a") as eqn_file:
                eqn_file.write(f"{eqn}\n")

    elif choice == "0":
        # run readfile eqn
        readfile()

    else:
        print("This is not an option, please try again")
        option_decision()


# create dict holding each function under string keys
operations_dict = {"multiply": [multiply, "x"],
                   "divide": [divide, "/"],
                   "add": [add, "+"],
                   "subtract": [minus, "-"],
                   }

option_decision()
