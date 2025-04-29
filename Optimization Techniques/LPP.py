from scipy.optimize import linprog

# Objective function coefficients (minimization)
c = [-3, -5]  # We use negatives for maximization

# Inequality constraints (A_ub * x <= b_ub)
A = [
    [1, 0],   # x <= 4
    [0, 2],   # 2y <= 12
    [3, 2]    # 3x + 2y <= 18
]
b = [4, 12, 18]

# Bounds (x >= 0, y >= 0)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve the problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Print results
if result.success:
    print("Optimal Solution:")
    print(f"x = {result.x[0]}, y = {result.x[1]}")
    print("Optimal Objective Value:", -result.fun)  # Convert back to maximization
else:
    print("No solution found")