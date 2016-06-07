class Cell(object):

    def __init__(self, x, y, timer, radius, camp):
        self.x = x
        self.y = y
        self.timer = timer
        self.radius = radius
        self.camp = camp
        self.move_vector = (0, 0)
