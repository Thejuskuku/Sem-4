import math
def forward_difference(f, x, h):

    return (f(x + h) - f(x)) / h

def F(x):
    return math.exp(x)

x0 = 1
h = 0.01
approx_derivative = forward_difference(F, x0, h)

print(f"Approximate derivative at x = {x0}: {approx_derivative}")
