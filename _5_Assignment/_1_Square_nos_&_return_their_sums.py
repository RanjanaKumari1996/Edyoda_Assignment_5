class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        self.sum=0
        self.sum+=self.x**2+self.y**2+self.z**2
        return self.sum

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=int(input("Enter third number: "))

square_sum=Point(x,y,z)
print("Sum of square numbers: ", square_sum.sqSum())