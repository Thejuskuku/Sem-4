import numpy as np

def gauss_seidel(A, b, tol=1e-6, max_iterations=100):
    n = len(b)
    x = np.zeros(n)  # Initial guess (zero vector)
    
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum1 = sum(A[i][j] * x_new[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        
        # Convergence check
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    
    print("Warning: Maximum iterations reached without convergence.")
    return x

# User input
n = int(input("Enter the number of equations: "))
A = []
b = []
print("Enter the augmented matrix row-wise:")
for i in range(n):
    row = list(map(float, input(f"Row {i + 1}: ").split()))
    A.append(row[:-1])  # Coefficient matrix
    b.append(row[-1])   # Constant terms

A = np.array(A, dtype=float)
b = np.array(b, dtype=float)

# Solving using Gauss-Seidel
solution = gauss_seidel(A, b)
print("Solution:", solution)
