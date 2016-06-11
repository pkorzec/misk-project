import cProfile
from Methods import simulation
from Methods import create_random_cells
from matplotlib import pyplot as plt

result = simulation(500, create_random_cells(500, 500, 1000), 25, 5, ((250, 250),))

f1 = plt.figure(1)
plt.matshow(result[0], fignum=1, cmap=plt.cm.gray)
f1.show()
f2 = plt.figure(1)
plt.matshow(result[1], fignum=1, cmap=plt.cm.gray)
f2.show()
f3 = plt.figure(1)
plt.matshow(result[2], fignum=1, cmap=plt.cm.gray)
f3.show()
f4 = plt.figure(1)
plt.matshow(result[3], fignum=1, cmap=plt.cm.gray)
f4.show()
