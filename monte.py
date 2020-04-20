import math, numpy, random

def estimate_integral(func, a, b):
    samples = 100
    ys = [(b-a)*func(random.random()) for s in range(samples)]
    return sum(ys) / len(ys)

def func1(x):
    return math.exp(x+x**2)

def func2(x):
    return numpy.sinc(x)

print(estimate_integral(func1, -2, 2))
