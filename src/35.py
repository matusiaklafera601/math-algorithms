# This is a randomly generated Python code for educational purposes.
def square_root(n):
    """
    Calculates the square root of a given number n using the Newton-Raphson method.
    
    Parameters:
        n (float): The number to find the square root of. Must be non-negative.
        
    Returns:
        float: The approximate square root of n.
    """
    if n < 0:
        raise ValueError("The input must be a non-negative number.")
    elif abs(n) == 1:
        return 1
    else:
        a = 3  # Initial guess for the square root
        b = (n + 1) / 2  # The middle point in the interval
    
        while True:
            c = (a * b) - n
            if abs(c) < 0.0001:
                return round(b, 5)
            else:
                a, b = b, c

# Example usage
result = square_root(9)
print(f"The square root of 9 is approximately: {result}")
