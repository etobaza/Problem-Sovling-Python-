class Shape:
    
    def __init__(self):
        self.length = 0

    def area(self):
        return 0

class Rectangle(Shape):

    def __init__(self, length, width):
        self.len = length
        self.wid = width

    def area(self):
        return self.len*self.wid

a = int(input("What's the length?: \n"))
b = int(input("What's the width?: \n"))
n = Rectangle(a, b)
print("Rectangle area is:", n.area())