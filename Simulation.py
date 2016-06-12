from Methods import simulation
from Methods import create_random_cells
from matplotlib import pyplot as plt
import numpy as np

cells = create_random_cells(100, 100, 100)

simulation(100, cells, 120, 5, ((25, 25), (75, 75)))

