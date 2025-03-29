def add(x, y):
    while True:
        try:
            result = x + y
            break
        except TypeError:
            x, y = y, int(input("Please enter a number: "))
    print(f"The sum of {x} and {y} is {result}")
add(3, 5)
