
class Calculator:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self):
        self.sum = self.y + self.x
        return self.sum 

    def subtract(self):
        self.subt = self.y - self.x
        return self.subt

    def multiply(self):
        self.mul = self.y * self.x
        return self.mul

    def divide(self):
        self.div = self.y / self.x
        return self.div


x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print(end="\n")

calculator_obj=Calculator(x,y)
print("Addition of numbers: ",calculator_obj.add())
print("Subtraction of numbers: ",calculator_obj.subtract())
print("Multiplication of numbers: ",calculator_obj.multiply())
print("Division of numbers: ",calculator_obj.divide())
