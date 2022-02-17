import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Current position of X1 and Y1:", self.x, self.y)

    def move(self, x, y):
        x = int(input("Change X1 to: "))
        y = int(input("Change Y1 to: "))
        self.x = x
        self.y = y
        
    def dist(self, x2, y2):
        return math.sqrt((x2-self.x)**2 + (y2 - self.y)**2)

x = int(input("Enter coordinate X1: "))
y = int(input("Enter coordinate Y1: "))
x2 = int(input("Enter coordinate X2: "))
y2 = int(input("Enter coordinate Y2: "))

n = Point(x, y)
n.show()
n.move(x, y)
n.show()
print("Distance between two points:", round(n.dist(x2, y2), 2))