from Ship import Ship


class InvisibleShip(Ship):

    def __init__(self, hitpoints):
        Ship.__init__(self, hitpoints)

    def get_hit(self, amount: int) -> None:
        pass


is1 = InvisibleShip(5)
is1.move_right()
is1.get_hit(77)
