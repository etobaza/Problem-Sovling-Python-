class Shape:
    def __init__(self):
        self.length = 0

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, len):
        self.length = len

    def area(self):
        return self.length**2

n = Square(int(input('len = ')))
print("Square is:", n.area())