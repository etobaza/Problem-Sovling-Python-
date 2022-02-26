import math 

def trp_area(h, b1, b2):
    return 1/2*(b1+b2)*h

height = int(input("Height: "))
base1 = int(input("Base 1: "))
base2 = int(input("Base 2: "))

print("Area of trapezoid:", trp_area(height, base1, base2))