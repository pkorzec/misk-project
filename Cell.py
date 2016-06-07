class Cell(object):

    def __init__(self, x, y, radius, camp):
        self.x = x
        self.y = y
        self.refractory_timer = -1
        self.firing_timer = -1
        self.radius = radius
        self.camp = camp
        self.move_vector = (0, 0)
