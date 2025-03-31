def sum_of_squares(n):
    """
    Calculate the sum of squares of first n natural numbers.
    
    Args:
    - n: An integer representing the number of natural numbers up to 10.
    
    Returns:
    - The sum of squares of first n natural numbers.
    """
    return (n * (n + 1) * (2 * n + 1)) // 6

# Example usage
result = sum_of_squares(10)
print(f"The sum of squares of the first 10 natural numbers is: {result}")
