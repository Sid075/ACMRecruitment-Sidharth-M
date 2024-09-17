import math
import re

class Calculator:
    def __init__(self):
        self.operators = {'+': self.add, '-': self.subtract, '*': self.multiply, '/': self.divide, '^': self.exponent}
        self.parentheses = ['(', ')']

    def calculate(self, expression):
        expression = self.preprocess(expression)
        try:
            result = self.evaluate_expression(expression)
            return result
        except Exception as e:
            raise ValueError("Error in calculation:",e)

    def preprocess(self, expression):
        expression = expression.replace('√', 'sqrt').replace('^', '**')
        expression = expression.replace(' ', '')
        return expression

    def evaluate_expression(self, expression):
        try:
            result = eval(expression, {"__builtins__": None}, self.operators)
            return result
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero is not allowed.")
        except Exception:
            raise ValueError("Malformed expression.")

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError("Division by zero.")
        return x / y

    def exponent(self, x, y):
        return x ** y

    def sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of a negative number.")
        return math.sqrt(x)


def main():
    calculator = Calculator()
    while True:
        expression = input("Enter an expression (or 'q' to quit): ")
        if expression.lower() == 'q':
            break
        try:
            result = calculator.calculate(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", str(e))


if __name__ == "__main__":
    main()
