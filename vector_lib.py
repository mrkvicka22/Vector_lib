from math import sqrt, cos, sin, radians, atan, degrees


class Vector2D:
    """A 2D vector that supports addition, calculation of magnitude
       and initialization from (magnitude, angle)."""

    def __init__(self, x, y):
        """Standard constructor with x and y components."""
        self.x = x
        self.y = y

    @classmethod
    def from_polar(cls, polar):
        """Alternative constructor from magnitude and angle from x-axis in degrees."""
        x = polar[1] * cos(radians(polar[0]))
        y = polar[1] * sin(radians(polar[0]))
        return cls(x, y)

    def __add__(self, other):
        """v1 + v2 if both are 2D vectors"""
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.x - other.x, self.y - other.y)

    def scalar_mul(self, scalar):
        return self.__class__(self.x * scalar, self.y * scalar)

    def dot_product(self, other):
        """v1 + v2 if both are 2D vectors"""
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.x * other.x + self.y * other.y)

    @property
    def magnitude(self):
        """Magnitude/length of vector"""
        return sqrt(self.x**2 + self.y**2)

    @property
    def angle(self):
        return degrees(atan(self.x/self.y))

    @property
    def polar(self):
        if self.y >= 0:
            return [degrees(atan(self.x/self.y)), self.magnitude]
        else:
            return [degrees(atan(self.x/self.y)), 0 - self.magnitude]

    def invert(self):
        return self.__class__(self.x * (-1), self.y * (-1))

    @property
    def lst(self):
        return [self.x, self.y]

'''NOT DONE!!!'''
class Vector3D:

    def __init__(self, x, y, z):
        """Standard constructor with x and y components."""
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """v1 + v2 if both are 2D vectors"""
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def scalar_mul(self, scalar):
        return self.__class__(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot_product(self, other):
        """v1 + v2 if both are 2D vectors"""
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.x * other.x, self.y * other.y, self.z * other.z)

    def cross_product(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def invert(self):
        return self.__class__(self.x * (-1), self.y * (-1), self.z * (-1))

    @property
    def magnitude(self):
        """Magnitude/length of vector"""
        return sqrt(self.x**2 + self.y**2)

    @property
    def lst(self):
        return [self.x, self.y, self.z]

if __name__ == '__main__':
    v = Vector3D(1, 1, 1)
    v2 = Vector3D(2, 3, 2)
    s = 2
    v3 = v.cross_product(v2)
    print(v3.lst)