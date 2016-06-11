import Constants


class Cell(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.relaying_refractory_timer = -1
        self.chemotaxis_refractory_timer = -1
        self.firing_timer = Constants.INFLUENCE_TIME + 1
        self.rand_move_timer = -1
        self.camp = 0
        self.coordinates = []
        self.is_autonomous = False

    def update(self, time_frame):

        if self.chemotaxis_refractory_timer > 0:
            self.chemotaxis_refractory_timer -= time_frame

        if self.relaying_refractory_timer > 0:
            self.relaying_refractory_timer -= time_frame

        if self.firing_timer < Constants.INFLUENCE_TIME:
            self.firing_timer += time_frame

        self.camp = 0

    def __str__(self):
        return '[%d, %d]' % (self.x, self.y)
