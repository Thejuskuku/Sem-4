def backward_difference(f, x, h):
    """Compute backward difference approximation of f'(x)"""
    return (f(x) - f(x - h)) / h

print("Backward Difference Derivative Calculator")
print("---------------------------------------")

print("Only use: +, -, *, /, ** (power)")
func_str = input("Enter function f(x) (e.g., x**3 - 2*x + 1): ")
f = lambda x: eval(func_str)

x = float(input("Enter x value: "))
h = float(input("Enter step size h (e.g., 0.001): "))

approx = backward_difference(f, x, h)
actual = (f(x + 1e-10) - f(x - 1e-10)) / (2e-10)  

error = abs(actual - approx)
rel_error = error/abs(actual) if actual != 0 else 0

print(f"\nResults at x = {x}:")
print(f"Backward difference (h={h}): {approx:.8f}")
print(f"More precise derivative: {actual:.8f}")
print(f"Absolute error: {error:.8f}")
print(f"Relative error: {rel_error:.2%}")