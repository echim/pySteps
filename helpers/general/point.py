class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x: int):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y: int):
        self._y = new_y
