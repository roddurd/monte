import math, numpy, random

def estimate_integral(func, a, b):
    samples = 1000000
    ys = [func(random.uniform(a,b)) for s in range(samples)]
    return (b-a)*sum(ys) / samples

def func1(x):
    return math.exp(x+x**2)

def func2(x):
    return numpy.sinc(x)

def func3(x):
    return 4*(1-x**2)**(0.5)

print(estimate_integral(func2, 0,4*math.pi))
