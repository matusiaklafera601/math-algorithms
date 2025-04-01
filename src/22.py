import numpy as np
from scipy.optimize import minimize

def f(x):
    return x**2 + 10*x

result = minimize(f, 0)
print("The function value at x=0 is:", result.fun)
