import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def bessel_function(x, c, s):
    """
    Bessel function of the first kind.
    
    Parameters:
    x (float): The independent variable.
    c (float): The parameter a in the formula.
    s (float): The parameter b in the formula.
    
    Returns:
    float: The value of the Bessel function at x.
    """
    return np.exp(-c * np.cos(x) / 2.0 - s * np.sin(x) + np.sqrt((1 - c**2) * (c + 3.0)))

def fit_bessel_function(data):
    """
    Fit a Bessel function to the given data points.
    
    Parameters:
    data (list): The data points [(x, y)] where x is the independent variable and y is the dependent variable.
    
    Returns:
    dict: A dictionary containing the parameters of the fitted Bessel function.
    """
    popt, _ = curve_fit(bessel_function, data[0], data[1])
    return {
        "c": popt[0],
        "s": popt[1]
    }

def plot_bessel_function(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bessel Function Plot')
    plt.show()

# Example data
data_points = [(-0.4529913687960893, 0.12267405418115473), (-0.4339950567591733, -0.03808936154965057),
               (-0.414526743671467, 0.04033317400759149), (0.0000000000000000, 0.0),
               (0.000281993470631435, -0.000334144410833819),
               (0.000590064664940803, 0.0), (0.0202708384998973, -0.047134873864035),
               (-0.8999699797686987, 0.2180598765335602), (0.7498814377171011, 0.0),
               (1.244933387140966, -1.439403593694643)]

# Fit the Bessel function to the data
result = fit_bessel_function(data_points)

print("Fitted parameters:", result)
