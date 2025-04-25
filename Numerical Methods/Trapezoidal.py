def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b)) 

    for i in range(1, n):
        total += f(a + i * h)
    
    return total * h

if __name__ == "__main__":
    
    def f(x):
        return x**2 + 3*x + 2
    
    a = 0
    b = 4
    n = 100 
    integral = trapezoidal_rule(f, a, b, n)
    
    print(f"Approximate integral using Trapezoidal Rule: {integral:.6f}")
    print(f"Exact integral value: {64/3 + 24 + 8:.6f}") 