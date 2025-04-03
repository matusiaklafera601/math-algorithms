def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    approx = 1.0
    while True:
        nearest_square = (num + approx) // 2
        if abs(approx**2 - num) < 0.0000001: 
            return nearest_square
        elif approx > num / 2:
            closest_less = (approx * approx)
            if abs(closest_less - num) < 0.0000001:
                return closest_less
            else:
                approx = nearest_square
        else:
            nearest_more = ((num - approx) // (nearest_square + 1))
            if abs(approx - nearest_more * (nearest_square + 1)) < 0.0000001:
                return approx

# Example usage: print(square_root(9)) should output approximately 3.0
