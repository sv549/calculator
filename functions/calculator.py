from functions.subtraction import subtraction
from functions.addition import addition
from functions.division import division
from functions.square import square
from functions.mutiply import multiply
from functions.squareroot import squareroot

class Calculator:
    ready = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a ,b)

    def subtraction(self, a, b):
        self.result = subtraction(a,b)

    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
