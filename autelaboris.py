import numpy as np
from scipy.interpolate import interp1d

# Define some data points
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Create an interpolation function
f = interp1d(x, y, kind='linear')

# Interpolate at a new point
x_new = 2.5
y_new = f(x_new)

print(y_new)  # Output: 6.5
