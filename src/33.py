def is_even(number):
    """
    Check if a number is even.
    
    Args:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is even, False otherwise.
    """
    return number % 2 == 0

print(is_even(4))  # Output: True
print(is_even(5))  # Output: False
