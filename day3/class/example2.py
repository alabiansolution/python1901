class Arithmatic:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        add = self.num1 + self.num2
        print("The addition of two numbers is", add)
    def mult(self):
        mult = self.num1 * self.num2
        print("The addition of two numbers is", mult)
    def div(self):
        div = self.num1 / self.num2
        print("The addition of two numbers is", div)

numbers = Arithmatic(4, 6)
numbers.add()
numbers.mult()
