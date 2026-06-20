import math
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def Area(self):
        return(math.pi * self.r**2)

class Cylinder(Circle):
    def __init__(self, x, y, r, h):
        Circle.__init__(self, x, y, r,)
        self.h = h
    def vol(self):
        return(self.Area() * self.h)

p = Cylinder(1, 1, 1, 2)
print(p.Area())
print(p.vol())
