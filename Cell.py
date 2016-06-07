class Cell(object):

    def __init__(self, x, y, timer, radius, cAMP):
        self.x = x
        self.y = y
        self.timer = timer
        self.radius = radius
        self.cAMP = cAMP
        self.fired_recently = False
