import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def f(x):
    """
    A simple quadratic function: f(x) = x^2 - 3x + 1
    """
    return x**2 - 3*x + 1

def gradient_descent(start_point, learning_rate=0.01):
    """
    Perform gradient descent to minimize the given function.
    
    Parameters:
        start_point: Initial point for gradient descent.
        learning_rate: Learning rate for gradient descent.
        
    Returns:
        The optimized value of x and the corresponding minimum point (x_min).
    """
    x, _ = np.min(f(np.array([start_point])), axis=0)
    result = minimize(lambda x: f(x), start_point, options={"maxiter": 100})
    
    return result.x, -result.fun

def main():
    # Initial starting point
    initial_point = [2.5]
    optimized_value, _ = gradient_descent(initial_point)

    print(f"Optimized value of x: {optimized_value[0]}")
    print(f"The minimum point (x_min): {f(optimized_value[0])}")

if __name__ == "__main__":
    main()
