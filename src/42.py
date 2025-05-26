def square_root(x):
    if x >= 0:
        y = x ** 0.5
        return round(y, 2)
    else:
        raise ValueError("Cannot calculate the square root of a negative number.")

# Example usage
try:
    print(square_root(16))
except ValueError as e:
    print(e)

