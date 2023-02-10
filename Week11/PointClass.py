import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, x_add: int, y_add: int) -> None:
        self.x = x_add + self.x
        self.y = y_add + self.y

    def distance(self, other_point: 'Point') -> float:
        a = (other_point.x - self.x) ** 2
        b = (other_point.y - self.y) ** 2
        ans = math.sqrt(a + b)
        return ans

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other_point: 'Point') -> bool:
        return isinstance(other_point, Point) and self.x == other_point.x and self.y == other_point.y


class Segment:

    def __init__(self, p1: 'Point', p2: 'Point'):
        self.p1 = p1
        self.p2 = p2

    def translate(self, dx: int, dy: int) -> None:
        self.p1.translate(dx, dy)
        self.p2.translate(dx, dy)

    def length(self) -> float:
        return self.p1.distance(self.p2)


#point = Point(3, 4)
#point.translate(5, -8)
#point2 = Point(0, 0)
#point.distance(point2)

p1 = Point(3, 4)
p2 = Point(5, 9)
print(p1 < p2)

p1 = (0, 2)
p2 = (8, 2)
line = Segment(p1, p2)
line.translate(4, 0)
print((p1.x, p1.y))
print((p2.x, p2.y))
print(line.length())
