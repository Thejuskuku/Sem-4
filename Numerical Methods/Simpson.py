def simpsons_13_rule(f, a, b, n):

    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's 1/3 Rule")
    
    h = (b - a) / n
    x = a
    total = f(a) + f(b)  
    

    for i in range(1, n):
        x += h
        if i % 2 == 0:
            total += 2 * f(x)  
        else:
            total += 4 * f(x)  
    
    return total * h / 3

if __name__ == "__main__":

    def f(x):
        return x**3 + 2*x**2 + 4*x + 1
    
    a = 0
    b = 2
    n = 4
    integral = simpsons_13_rule(f, a, b, n)
    
    print(f"Approximate integral using Simpson's 1/3 Rule: {integral:.6f}")