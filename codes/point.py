import numpy as np
from ctypes import *
import matplotlib.pyplot as plt
import os

# Create the 'fig' directory if it doesn't exist
if not os.path.exists('fig'):
    os.makedirs('fig')
multip = CDLL('./point.so')
A = np.array([7, -1], dtype=np.double)
B = np.array([-3, -4], dtype=np.double)
C = np.zeros(2, dtype=np.double)
n = 2 / 3
point = multip.point
point.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_double]
point(A.ctypes.data_as(POINTER(c_double)), 
      B.ctypes.data_as(POINTER(c_double)), 
      C.ctypes.data_as(POINTER(c_double)), 
      c_double(n))
num_points = 10 
result = np.zeros((num_points, 2), dtype=np.double)
generate_points = multip.generate_points
generate_points.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double), c_int]
generate_points(A.ctypes.data_as(POINTER(c_double)),
                B.ctypes.data_as(POINTER(c_double)),
                result.ctypes.data_as(POINTER(c_double)),
                c_int(num_points))

# Combine A, B, and C into a single array for plotting
tri_coords = np.array([A, B, C]).reshape(3, 2)

# Plotting all lines
plt.plot(result[:, 0], result[:, 1], label='$AB$')  # Plot line segment AB
plt.scatter(tri_coords[:, 0], tri_coords[:, 1], color='red')  # Scatter plot of points

# Adding labels for points
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[i, 0]:.0f}, {tri_coords[i, 1]:.0f})',
                 (tri_coords[i, 0], tri_coords[i, 1]),
                 textcoords="offset points",
                 xytext=(20, -10),
                 ha='center')

# Customize axes
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

# Save the figure in the 'fig' directory
plt.savefig('fig/fig.jpg')
plt.show()  # Show the plot

