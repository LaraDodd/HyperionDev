from typing import Callable, Union

"""defensive programming calculator program"""


def add(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations_dict = {"multiply": multiply,
                   "divide": divide,
                   "add": add,
                   "subtract": minus,
                   }


def calculator(operation: Callable, n1: int, n2: int) -> Union[float, int]: #type annotating
    return operation(n1, n2)

def run_calculator():
    try:
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))
    except ValueError as error:
        print(f"{error} is not a number, please enter a number")
        run_calculator()
    else:
        operation = input("Would you like to multiply, divide, add or subtract the first number from the second? ")

        try:
            print(calculator(operations_dict[operation], num1, num2))
        except KeyError:
            print("This operation does not exist, try again")
            run_calculator()
            # call calculator?
        except ZeroDivisionError:
            print("You cannot divide by zero, try again")
            run_calculator()




run_calculator()
# errors:
# type annotations
#zero division error
#key valye
