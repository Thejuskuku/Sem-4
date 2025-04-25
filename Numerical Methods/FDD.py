def forward_difference(f, x, h):
    """Compute forward difference approximation of f'(x)"""
    return (f(x + h) - f(x)) / h

print("Forward Difference Derivative Calculator")
print("--------------------------------------")

print("Only use these operations: +, -, *, /, ** (power)")
func_str = input("Enter function f(x) (e.g., x**2 + 3*x - 5): ")
f = lambda x: eval(func_str)

x = float(input("Enter x value where to calculate derivative: "))
h = float(input("Enter step size h (e.g., 0.001): "))

approx = forward_difference(f, x, h)

actual = forward_difference(f, x, h=1e-10)

error = abs(actual - approx)
rel_error = error/abs(actual) if actual != 0 else 0

print(f"\nResults at x = {x}:")
print(f"Approximate derivative (h={h}): {approx:.8f}")
print(f"More precise derivative: {actual:.8f}")
print(f"Absolute error: {error:.8f}")
print(f"Relative error: {rel_error:.2%}")