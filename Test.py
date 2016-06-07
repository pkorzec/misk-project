import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# def samplemat(dims):
#     """Make a matrix with all zeros and increasing elements on the diagonal"""
#     aa = np.zeros(dims)
#     for i in range(min(dims)):
#         aa[i, i] = i
#     return aa
#
# # Display 2 matrices of different sizes
# dimlist = [(12, 12), (15, 35)]
# for d in dimlist:
#     plt.matshow(samplemat(d))

# Display a random matrix with a specified figure number and a grayscale
# colormap
# plt.matshow(np.random.rand(1000, 1000), fignum=100, cmap=plt.cm.afmhot)
#
# plt.show()

i = Image.new("RGB", (100, 100)).show()

