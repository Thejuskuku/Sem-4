def second_derivative_CDD(f, x, h):
    """Compute second derivative using central divided difference"""
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)

print("Second Derivative Calculator (Central Difference Method)")
print("-----------------------------------------------------")

print("Only use: +, -, *, /, ** (power)")
func_str = input("Enter function f(x) (e.g., x**3 - 2*x + 1): ")
f = lambda x: eval(func_str)

x = float(input("Enter x value: "))
h = float(input("Enter step size h (e.g., 0.001): "))

approx = second_derivative_CDD(f, x, h)
actual = (f(x + 1e-6) - 2*f(x) + f(x - 1e-6)) / (1e-6)**2  

error = abs(actual - approx)
rel_error = error/abs(actual) if actual != 0 else 0

print(f"\nResults at x = {x}:")
print(f"CDD second derivative (h={h}): {approx:.8f}")
print(f"More precise reference: {actual:.8f}")
print(f"Absolute error: {error:.8f}")
print(f"Relative error: {rel_error:.2%}")