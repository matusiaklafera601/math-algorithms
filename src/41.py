import numpy as np
from scipy.optimize import fsolve

def equation(x):
    # Your function here
    return x ** 2 - 3 * x + 1

x_values = np.linspace(-5, 5, 400)
equations = [fsolve(equation, val) for val in x_values]

for i in range(len(x_values)):
    print(f"X: {x_values[i]}, Y: {equations[i]}")
