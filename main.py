from random import random, randint


class Field():
    def __init__(self, field, hid=False):
        self.field = field
        self.hid = hid
        self.field = [[" "] * 6 for i in range(6)]

    def __str__(self):

    res = "    | 1 | 2 | 3 | 4 | 5 | 6 | "
    for i, row in enumerate(self.field):
        res += f"\n{i + 1} | " + " | ".join(row) + " | "
    if self.hid:
        res = res.replace("■", "O")

    def add_ship(self):


class Dot:  # coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, smallship, v, h, health=1) -> None:
        self.smallship = smallship  # one "dot"
        self.SetPos(smallship)
        self.h = h  # horizontal
        self.v = v  # vertical
        self.setcolor(0)
        self.health = health

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPos(self, smallship):
        self.smollship = smallship

    def getPos(self):
        return self.smollship

    def isIn(self, x, y) -> bool:
        return False


class Fleet(Ship):
    def __init__(self, pos, w, h):  # позиция, ширина, длинна корабля
        super().__init__(pos)
        self.w = w
        self.h = h
        self.w = 1
        # def getWidth(self):

    #     return self.w

    def getHeight(self):
        return self.h

    def isIn(self, x, y):
        _pos = super().getPos()
        if (_pos.x < x) and ((_pos.x + self.w) > x) and (_pos.y < y) and ((_pos.y + self.h) > y):
            return True
        return False


class TwoShip(Ship):
    pass


class Game_gen:
    pass


class User:
    pass
