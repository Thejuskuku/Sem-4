def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def F(x):
    return x**3 + 2*x**2 - 5*x + 7

x0 = 2  
h = 0.1 

approx_derivative = forward_difference(F, x0, h)

print(f"Approximate derivative at x = {x0}: {approx_derivative}")
