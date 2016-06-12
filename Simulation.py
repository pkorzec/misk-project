from Methods import simulation
from Methods import create_random_cells

frame_time = 5
n_of_cells = 500
iterations = 120
size = 200
cells = create_random_cells(size, n_of_cells)
centers = ((30, 30), (70, 70))

simulation(size, cells, iterations, frame_time, centers)
