def euler_method(f, x0, y0, h, x_end):
 
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < x_end:
        x = x_values[-1]
        y = y_values[-1]

        y_new = y + h * f(x, y)
        x_new = x + h
        
        x_values.append(x_new)
        y_values.append(y_new)
    
    return x_values, y_values

if __name__ == "__main__":
    
    def f(x, y):
        return x + y  

    x0 = 0
    y0 = 1

    h = 0.1
    x_end = 1.0

    x_vals, y_vals = euler_method(f, x0, y0, h, x_end)
    print("Euler's Method Solution:")
    print("x\t\ty(x)")
    for x, y in zip(x_vals, y_vals):
        print(f"{x:.2f}\t\t{y:.6f}")