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
def line_gen(A, B):
    length = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim, length))
    lam_1 = np.linspace(0, 1, length)
    for i in range(length):
        temp1 = A + lam_1[i] * (B - A)
        x_AB[:, i] = temp1.T
    return x_AB
x_AB = line_gen(A, B)

# Debugging output for line segment coordinates
print("Line segment coordinates (x_AB):", x_AB)

# Plotting all lines
plt.plot(x_AB[0, :], x_AB[1, :], label='$AB$')

# Combine A, B, and C into a single array for plotting
tri_coords = np.array([A, B, C]).reshape(3, 2)

# Print tri_coords for debugging
print("tri_coords for plotting:", tri_coords)

# Plotting the points
plt.scatter(tri_coords[:, 0], tri_coords[:, 1], color='red')  # Scatter plot of points
vert_labels = ['A', 'B', 'C']
for i, txt in enumerate(vert_labels):
    plt.annotate(f'{txt}\n({tri_coords[i, 0]:.0f}, {tri_coords[i, 1]:.0f})',
                 (tri_coords[i, 0], tri_coords[i, 1]),  # point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(20, -10),  # distance from text to points (x, y)
                 ha='center')  # horizontal alignment

# Customize axes
ax = plt.gca()
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
plt.legend(loc='best')
plt.grid()  # minor
plt.axis('equal')

# Save the figure in the 'fig' directory
plt.savefig('fig/fig.jpg')
plt.show()  # Show the plot'''

