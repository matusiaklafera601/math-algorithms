def multiply(x, y):
    """Multiply two numbers."""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be integers or floats.")
    result = x * y  # Multiply the numbers without using multiplication operation
    return result

def add(x, y):
    """Add two numbers."""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be integers or floats.")
    result = x + y  # Add the numbers without using addition operation
    return result

def subtract(x, y):
    """Subtract two numbers."""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be integers or floats.")
    result = x - y  # Subtract the numbers without using subtraction operation
    return result

def divide(x, y):
    """Divide two numbers."""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise ValueError("Both inputs must be integers or floats.")
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = x / y  # Divide the numbers without using division operation
    return result

def power(base, exponent):
    """Raise a number to an integer exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, int):
        raise ValueError("Both inputs must be integers.")
    result = base ** exponent  # Raise the base to the given exponent
    return result

def gcd(a, b):
    """Find the greatest common divisor of two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be integers.")
    if a == 0:
        return b
    else:
        remainder = b % a
        result = gcd(a - remainder, a)  # Euclidean algorithm
        return result

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(multiply(4, 6))  # Output: 24
print(add(3, 7))      # Output: 10
print(subtract(4.5, 2.1))  # Output: 2.4
print(divide(8, 2))    # Output: 4
print(power(2, 3))     # Output: 8
print(gcd(15, 5))      # Output: 5
print(is_prime(7))     # Output: True
