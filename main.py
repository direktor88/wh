from random import random, randint


class Field():
    def __init__(self, field, hid=False):
        self.field = field
        self.hid = hid
        self.field = [[" "] * 6 for i in range(6)]
    #     print("    | 1 | 2 | 3 | 4 | 5 | 6 | ")
    # print("  --------------------------- ")
    # for i, row in enumerate(field):
    #     row_str = f"  {i + 1} | {' | '.join(row)} | "
    #     print(row_str)
    #     print("  --------------------------- ")


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __init__(self, smallship) -> None:
        self.SetPos(smallship)

    def setPos(self, smallship):
        self.smollship = smallship

    def getPos(self):
        return self.smollship

    def isIn(self, x, y) -> bool:
        return False

class Fleet(Ship):
    def __init__(self, pos, w, h):
        super().__init__(pos)
        self.w = w
        self.h = h
    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def isIn(self, x , y):
        _pos = super().getPos()
        if (_pos.x < x) and ((_pos.x + self.w)>x ) and (_pos.y < y) and ((_pos.y + self.h) > y):
            return True
        return False




class TwoShip(Ship):
    pass


class Game_gen:
    pass


class User:
    pass


