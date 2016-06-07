import Constants
import math
from decimal import Decimal
from random import randint
from Cell import Cell
from matplotlib import pyplot as plt
import numpy as np

RADIUS_SCALE = 1e3
INFLUENCE_RADIUS = 0.300


def simulation(size, cells):
    environment = np.zeros(size, size)

    for cell in cells:
        environment[cell.x, cell.y] += 1


def simulation_frame(cells, frame_time):

    is_ready_to_fire = True
    is_sensitive = True
    firing_queue = []
    environment = np.zeros(1000, 1000)

    for cell in cells:
        environment[cell.x, cell.y] += 1

    for i in range(len(cells)):

        current_cell = cells[i]

        if is_autonomous(current_cell, environment):

            if is_ready_to_fire:
                firing_queue.append(current_cell)
                current_cell.timer = Constants.RELAYING_REFRACTORY_PERIOD

        else:

            if is_sensitive:

                for firing_cell in firing_queue:

                    radius = calculate_radius((current_cell.x, current_cell.y), (firing_cell.x, firing_cell.y)) / \
                        RADIUS_SCALE

                    if fired_recently(firing_cell) and radius < INFLUENCE_RADIUS:

                        current_cell.camp += calculate_camp_concentration(radius, firing_cell.firing_timer)

                # TODO calculate gradient, chose destination with highest, move cell one step at a time
                if current_cell.camp > Constants.CHEMOTAXIS_THRESHOLD:
                    move_cell(current_cell, environment)

    return 0


# TODO not sure if that's correct way of checking autonomy
def is_autonomous(cell, environment):

    return environment[cell.x, cell.y] == 1


def fired_recently(cell):

    return cell.firing_timer


def move_cell(cell, environment, destination=(0, 0)):

    environment[cell.x, cell.y] -= 1

    cell.x = destination[0]
    cell.y = destination[1]

    environment[cell.x, cell.y] += 1


def calculate_camp_concentration(r, t):

    t = Decimal(str(t))
    r = Decimal(str(r))

    n = Constants.N_OF_RELEASED_MOLECULES
    a = Decimal.exp(-((r ** 2) / (4 * Constants.DIFFUSION_CONSTANT * t)))
    b = Decimal.exp(-(t / Constants.TAU))
    c = Decimal(4 * Decimal(math.pi) * t * Constants.DIFFUSION_CONSTANT) ** (Decimal(2) / Decimal(3))

    return (n * a * b) / c


def calculate_gradient(r, t):

    t = Decimal(str(t))
    r = Decimal(str(r))

    concentration = calculate_camp_concentration(r, t)

    return (2 * concentration * r) / (4 * Constants.DIFFUSION_CONSTANT * t)


def calculate_radius(start, end):

    return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)


def create_random_cells(length, height, n_of_cells):
    result = [0] * n_of_cells

    for i in range(n_of_cells):
        x = randint(0, length - 1)
        y = randint(0, height - 1)

        result[i] = Cell(x, y, 0, 0)

    return result


# m = np.zeros((1000, 1000))
#
# cells = create_random_cells(1000, 1000, 20000)
#
# for c in cells:
#     m[c.x, c.y] += 1
#
# plt.matshow(m, cmap=plt.cm.gray)
# plt.show()
#
# yaxis = [Decimal(0)] * 1000
# xaxis = [i for i in range(1000)]
# yaxis2 = [Decimal(8e-9)] * 1000
# yaxis3 = [Decimal(8e-9)] * 1000
#
#
# for i in range(1, 1000):
#     yaxis[i] = calculate_camp_concentration(0.280, i)
#
# for i in range(1, 1000):
#     yaxis3[i] = calculate_camp_concentration(0.250, i)
#
# plt.figure(1)
# plt.plot(xaxis, yaxis)
# plt.plot(xaxis, yaxis2)
# plt.plot(xaxis, yaxis3)
# plt.show()
