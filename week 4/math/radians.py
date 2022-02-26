import math

def toRadian(n):
    return (math.pi/180)*n

deg = int(input("Degrees: "))
print("In radians:", toRadian(deg))

