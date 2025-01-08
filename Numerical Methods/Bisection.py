def bisection_method(func, a, b, tol=1e-6, max_iter=100):  
    # Ensure that f(a) and f(b) have opposite signs
    if func(a) * func(b) > 0:
        print("The function must have opposite signs at the endpoints a and b.")
        return None
    
    iter_count = 0
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0 
        if func(c) == 0:  # Exact root found
            return c
        elif func(c) * func(a) < 0:  # Root is in the left half
            b = c
        else:  # Root is in the right half
            a = c

        iter_count += 1
        if iter_count >= max_iter:
            print("Max iterations reached.")
            break
    return (a + b) / 2.0

if __name__ == "__main__":
    def func(x):
        return x**2 - x - 6
    a = eval(input("Enter the left endpoint : "))
    b = eval(input("Enter the right endpoint : "))
    tolerance = 1e-6
    root = bisection_method(func, a, b, tol=tolerance)
    
    print(f"The approximate root is: {root}")
