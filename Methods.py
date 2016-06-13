import Constants
import math
from random import randint
from Cell import Cell
from Bresenham import get_line
from matplotlib import pyplot as plt
import numpy as np
from cdecimal import Decimal


def simulation(size, cells, iterations, frame_time, centers=((500, 500),)):

    environment = np.zeros((size, size))
    firing_queue = []

    for coordinates in centers:
        cell = Cell(coordinates[0], coordinates[1])
        cells.append(cell)
        cell.is_autonomous = True

    for cell in cells:
        environment[cell.x, cell.y] += 1

    for iteration in range(iterations):
        print 'iteration %d' % iteration

        simulation_frame(cells, frame_time, environment, firing_queue)

        plt.matshow(environment, fignum=(iteration + 1), cmap=plt.cm.gray)
        plt.savefig('Results/%d-seconds.png' % ((iteration + 1) * 5))
        plt.close()

        tmp = []

        for cell in firing_queue:
            if cell.firing_timer < Constants.INFLUENCE_TIME:
                tmp.append(cell)

        firing_queue = tmp

    return 0


def simulation_frame(cells, frame_time, environment, firing_queue):

    for z in range(len(cells)):

        current_cell = cells[z]

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

                max_gradient = -1
                coordinates = ()

                for firing_cell in firing_queue:

                    radius = calculate_radius((current_cell.x, current_cell.y), (firing_cell.x, firing_cell.y)) / \
                        Constants.RADIUS_SCALE

                    firing_influence = firing_cell.firing_timer

                    if firing_influence < Constants.INFLUENCE_TIME and radius < Constants.INFLUENCE_RADIUS:

                        result = calculate_gradient(radius, firing_influence)

                        gradient = result['gradient']
                        camp = result['camp']

                        if current_cell.camp < Constants.RELAYING_THRESHOLD:
                            current_cell.camp += camp

                        if gradient > max_gradient:
                            max_gradient = gradient
                            coordinates = (firing_cell.x, firing_cell.y)

                if current_cell.camp > Constants.CHEMOTAXIS_THRESHOLD and len(current_cell.coordinates) == 0:

                    current_cell.chemotaxis_refractory_timer = Constants.CHEMOTAXIS_REFRACTORY_PERIOD
                    movement_vector = get_line((current_cell.x, current_cell.y), (coordinates[0], coordinates[1]), 20)
                    current_cell.coordinates = movement_vector
                    current_cell.coordinates.pop(0)

                if current_cell.camp > Constants.RELAYING_THRESHOLD:
                    if is_ready_to_fire:
                        firing_queue.append(current_cell)
                        current_cell.relaying_refractory_timer = Constants.RELAYING_REFRACTORY_PERIOD
                        current_cell.firing_timer = 1

        cell_coord = current_cell.coordinates
        if len(cell_coord) > 0:
            if environment[cell_coord[0][0], cell_coord[0][1]] == 0:
                # print 'Current cell: ', current_cell, 'dest: ', current_cell.coordinates[0]
                move_cell(current_cell, environment, current_cell.coordinates[0])

            current_cell.coordinates.pop(0)

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
    a = Decimal.exp(-((r ** Decimal(2)) / (Decimal(4) * Constants.DIFFUSION_CONSTANT * t)))
    b = Decimal.exp(-(t / Constants.TAU))
    c = Decimal(4 * Decimal(math.pi) * t * Constants.DIFFUSION_CONSTANT) ** (Decimal(2) / Decimal(3))

    return (n * a * b) / c


def calculate_gradient(r, t):

    t = Decimal(str(t))
    r = Decimal(str(r))

    concentration = calculate_camp_concentration(r, t)
    gradient = (2 * concentration * r) / (4 * Constants.DIFFUSION_CONSTANT * t)

    return {'gradient': gradient, 'camp': concentration}


def calculate_radius(start, end):

    return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)


def create_random_cells(size, n_of_cells):
    result = [0] * n_of_cells

    for i in range(n_of_cells):
        x = randint(0, size - 1)
        y = randint(0, size - 1)

        result[i] = Cell(x, y)

    return result


# m = np.zeros((1000, 1000))
#
# cells = create_random_cells(1000, 1000, 20000)
#
# for c in cells:
#     m[c.x, c.y] += 1
#
# plt.matshow(m, fignum=100, cmap=plt.cm.gray)
# plt.show()

# yaxis = [Decimal(0)] * 1000
# xaxis = [i for i in range(1000)]
# yaxis2 = [Decimal(8e-9)] * 1000
# yaxis3 = [Decimal(8e-9)] * 1000
#
#
# for i in range(1, 1000):
#     yaxis[i] = calculate_gradient(0.240, i)['gradient']
#
# for i in range(1, 1000):
#     yaxis3[i] = calculate_camp_concentration(0.240, i)
#
# plt.figure(1)
# plt.plot(xaxis, yaxis)
# plt.plot(xaxis, yaxis2)
# plt.plot(xaxis, yaxis3)
# plt.show()
