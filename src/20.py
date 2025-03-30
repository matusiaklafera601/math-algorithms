def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Example usage
result = add(10, 5)
print("Addition result:", result)

result = subtract(10, 5)
print("Subtraction result:", result)

result = multiply(4, 3)
print("Multiplication result:", result)

result = divide(10, 2)
print("Division result:", result)
