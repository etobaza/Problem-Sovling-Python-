import math 

def area(n, s):
    return (n*s**2)/(4*math.tan(math.pi/n))

n = int(input("Sides: "))
length = int(input("Length of a side: "))
print("Area of the Regular Polygon:", area(n, length))