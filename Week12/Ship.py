class Ship:

    def __init__(self, hitpoints: int):
        self.hitpoints = hitpoints
        self.location = 0

    def move_left(self) -> None:
        self.location -= 1
        print(self.location)

    def move_right(self) -> None:
        self.location += 1
        print(self.location)

    def get_hit(self, amount: int) -> None:
        self.hitpoints -= amount
        print(self.hitpoints)

    def __repr(self) -> None:
        return f'({'locantion: ' + {self.location}, + 'hitpoints: ' + {self.hitpoints})'


s1 = Ship(5)
s1.move_right()
s1.move_right()
s1.get_hit(7)
print(s1)