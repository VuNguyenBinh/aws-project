def calc(a, b):
    return a + b

def calc_duplicate(a, b):  # duplicate of calc()
    return a + b

def long_function():
    x = 0
    for i in range(0, 500):
        x += i  # long, useless loop
    return x
