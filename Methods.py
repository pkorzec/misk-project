import Constants
import math
from decimal import Decimal
from random import randint
from Cell import Cell
from matplotlib import pyplot as plt
import numpy as np


def simulation(size, cells):
    environment = np.zeros(size, size)

    for cell in cells:
        environment[cell.x, cell.y] += 1


def algorithm_for_single_cell(cells):

    is_ready_to_fire = True
    is_sensitive = True
    fired_recently = False
    firing_queue = []
    environment = np.zeros(1000, 1000)

    for cell in cells:
        environment[cell.x, cell.y] += 1

    for i in range(len(cells)):

        current_cell = cells[i]

        if is_autonomous(current_cell, environment):

            if is_ready_to_fire:
                firing_queue.append(current_cell)
                current_cell.timer = Constants.relaying_refractory_period

        else:

            if is_sensitive:

                for firing_cell in firing_queue:
                    if fired_recently:

                        radius = calculate_radius(current_cell.x, current_cell.y,
                                                  firing_cell.x, firing_cell.y)

                        current_cell.camp += calculate_camp_concentration()



    return 0


# TODO not sure if that's correct way of checking autonomy
def is_autonomous(cell, environment):

    return environment[cell.x, cell.y] == 1


def move_cell(cell, environment, destination=(0, 0)):

    environment[cell.x, cell.y] -= 1

    cell.x = destination[0]
    cell.y = destination[1]

    environment[cell.x, cell.y] += 1


def calculate_camp_concentration(r, t):

    t = Decimal(str(t))
    r = Decimal(str(r))

    n = Constants.n_of_molecules_released
    a = Decimal.exp(-((r ** 2) / (4 * Constants.diffusion_constant * t)))
    b = Decimal.exp(-(t / Constants.tau))
    c = Decimal(4 * Decimal(math.pi) * t * Constants.diffusion_constant) ** (Decimal(2) / Decimal(3))

    return (n * a * b) / c


def calculate_gradient(r, t):

    t = Decimal(str(t))
    r = Decimal(str(r))

    concentration = calculate_camp_concentration(r, t)

    return (2 * concentration * r) / (4 * Constants.diffusion_constant * t)


def calculate_radius(x0, y0, x1, y1):

    return math.sqrt((x1 - x0) ** 2 + (y0 - y1) ** 2) / 10e3


def create_random_cells(length, height, n_of_cells):
    result = [0] * n_of_cells

    for i in range(n_of_cells):
        x = randint(0, length - 1)
        y = randint(0, height - 1)

        result[i] = Cell(x, y, 0, 0, 0)

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
#     yaxis[i] = calculate_camp_concentration(0.250, i)
#
# for i in range(1, 1000):
#     yaxis3[i] = calculate_camp_concentration(0.240, i)
#
# plt.figure(1)
# plt.plot(xaxis, yaxis)
# plt.plot(xaxis, yaxis2)
# plt.plot(xaxis, yaxis3)
# plt.show()

print calculate_radius(0,0,200,200)
