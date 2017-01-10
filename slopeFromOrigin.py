class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # TODO define a method called slopeFromOrigin here
    def slopeFromOrigin(self):
        x = self.x
        if x == 0:
            return None
        y = self.y
        m = y / x
        return m
