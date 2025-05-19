def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1 or n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence

# Example usage
print(fibonacci(10))
