def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def binomial_coefficient(n, k):
    if n < k or k < 0:
        return 0
    if n == k or k == 0:
        return 1
    else:
        return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)
