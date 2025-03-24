import numpy as np
from scipy.optimize import minimize

def f(x):
    return 0.5 * x[0]**2 + 3 * x[1]

x0 = [0.0, 0.0]  # Initial guess for the optimization problem

# Use a user-defined function to optimize
result = minimize(f, x0)
print(result)
