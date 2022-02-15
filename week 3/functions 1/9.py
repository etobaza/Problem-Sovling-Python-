def sphereVolume(r):
    volume = (4/3)*3.14159265359*r**3
    return round(volume, 2)
r = int(input())
print(sphereVolume(r))