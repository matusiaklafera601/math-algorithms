def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
    return total

result = calculate_sum(10)
print(result)
