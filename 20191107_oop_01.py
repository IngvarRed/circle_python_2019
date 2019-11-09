#

class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):  # 1
        return Vector2D(self.x + other.x, self.y + other.y)

    def __add__(self, other):  # 2
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        if type(scalar) is int or type(scalar) is float:
            return Vector2D(self.x * scalar, self.y * scalar)
        if type(scalar) is type(self):
            return self.x * scalar.x + self.y * scalar.y

    def modul(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value

    def __str__(self):
        return f"({self.x}, {self.y})"


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        # self.x = x
        # self.y = y
        super().__init__(x, y)
        self.z = z

    def __add__(self, other):


first = Vector2D(2, 3)
second = first * 2
print(first)
print(second)
print(second.modul())
#
print("*" * 30)
print(second[0])
second[0] = 5
print(second)
print("*" * 30)

third = first * second
print(third)

# 1
fourth = first.add(second)
print(fourth)
# 2
fourth = first + second
print(fourth)

print(fourth == second)

v3 = Vector3D(3, 4, 5)
print(v3.x, v3.y, v3.z)
