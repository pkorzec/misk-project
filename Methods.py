import Constants
import math
from decimal import Decimal
from random import randint
from Cell import Cell
from Queue import Queue
from matplotlib import pyplot as plt
import numpy as np


def simulation(size, cells):

    environment = np.zeros(size, size)

    for cell in cells:
        environment[cell.x, cell.y] += 1


def create_random_cells(length, height, n_of_cells):
    result = [0] * n_of_cells

    for i in range(n_of_cells):
        x = randint(0, length - 1)
        y = randint(0, height - 1)

        result[i] = Cell(x, y, 0, 0, 0)

    return result


def algorithm_for_single_cell(cells):

    is_autonomous = True
    is_ready_to_fire = True
    is_sensitive = True
    firing_queue = Queue

    for i in range(len(cells)):

        current_cell = cells[i]

        for cell in cells:
            if current_cell is not cell and current_cell.x == cell.x and current_cell.y == cell.y:
                is_autonomous = False
                break

        if is_autonomous:
            if is_ready_to_fire:
                firing_queue.put(current_cell)
                # set clock
            else:
                break
        else:
            if is_sensitive:
                cell = firing_queue

            else:
                break

    return 0


def calculate_camp_concentration(r, t):

    t = Decimal(str(t))
    r = Decimal(str(r))

    n = Constants.n_of_molecules_released
    a = Decimal.exp(-((r ** 2) / (4 * Constants.diffusion_constant * t)))
    b = Decimal.exp(-(t / Constants.tau))
    c = Decimal(4 * Decimal(math.pi) * t * Constants.diffusion_constant) ** (Decimal(2) / Decimal(3))

    return (n * a * b) / c


# TODO not sure if that's correct way of checking autonomy
def check_if_autonomous(cell, environment):

    return environment[cell.x, cell.y] == 1


def calculate_gradient(r, t):

    t = Decimal(str(t))
    r = Decimal(str(r))

    concentration = calculate_camp_concentration(r, t)

    return (2 * concentration * r) / (4 * Constants.diffusion_constant * t)


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
