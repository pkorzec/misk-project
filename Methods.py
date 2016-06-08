import Constants
import math
from decimal import Decimal
from random import randint
from Cell import Cell
from matplotlib import pyplot as plt
import numpy as np


def simulation(size, cells, centers):

    environment = np.zeros(size, size)

    for cell in cells:
        environment[cell.x, cell.y] += 1


def simulation_frame(cells, frame_time):

    firing_queue = []
    environment = np.zeros(1000, 1000)

    for cell in cells:
        environment[cell.x, cell.y] += 1

    for i in range(len(cells)):

        current_cell = cells[i]

        current_cell.update(frame_time)

        is_ready_to_fire = current_cell.relaying_refractory_timer <= 0
        is_sensitive = current_cell.chemotaxis_refractory_timer <= 0

        if current_cell.is_autonomous:

            if is_ready_to_fire:
                firing_queue.append(current_cell)
                current_cell.relaying_refractory_timer = Constants.RELAYING_REFRACTORY_PERIOD
                current_cell.firing_timer = 1

        else:

            if is_sensitive:

                max_gradient = 0
                coordinates = ()

                for firing_cell in firing_queue:

                    radius = calculate_radius((current_cell.x, current_cell.y), (firing_cell.x, firing_cell.y)) / \
                        Constants.RADIUS_SCALE

                    firing_influence = current_cell.firing_timer

                    if firing_influence < Constants.INFLUENCE_TIME and radius < Constants.INFLUENCE_RADIUS:

                        camp = calculate_camp_concentration(radius, firing_influence)

                        current_cell.camp += camp

                        gradient = calculate_gradient(radius, firing_influence)

                        if gradient > max_gradient:
                            max_gradient = gradient
                            coordinates = (firing_cell.x, firing_cell.y)

                # TODO calculate gradient, chose destination with highest, move cell one step at a time
                if current_cell.camp > Constants.CHEMOTAXIS_THRESHOLD:
                    move_cell(current_cell, environment, coordinates)

                if current_cell.camp > Constants.RELAYING_THRESHOLD:
                    if is_ready_to_fire:
                        firing_queue.append(current_cell)
                        current_cell.relaying_refractory_timer = Constants.RELAYING_REFRACTORY_PERIOD
                        current_cell.firing_timer = 1

    return 0


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
