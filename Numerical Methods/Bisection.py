import sympy as sp

def bisection(func, a, b, tol=1e-6, max_iter=100):  
    if func(a) * func(b) > 0:
        print("The function must have opposite signs at the endpoints a and b.")
        return None
    
    iter_count = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iter_count += 1
        if iter_count >= max_iter:
            print("Max iterations reached.")
            break
    return (a + b) / 2.0

def get_function():
    func_input = input("Enter the function : ")
    x = sp.symbols('x')
    func_expr = sp.sympify(func_input)
    func_lambda = sp.lambdify(x, func_expr, 'numpy')
    return func_lambda

if __name__ == "__main__":     
    func = get_function()
    a = eval(input("Enter the left endpoint : "))
    b = eval(input("Enter the right endpoint : "))
    tolerance = 1e-6
    root = bisection(func, a, b, tol=tolerance)
    
    print(f"The approximate root is: {root}")

"""
Enter the function : x**2 - x - 6
Enter the left endpoint : 0
Enter the right endpoint : 3
The approximate root is: 2.9999992847442627
"""