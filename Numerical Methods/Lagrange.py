def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    result = 0.0
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    
    return result

if __name__ == "__main__":
    
    x_data = [0, 1, 3, 5]
    y_data = [1, 3, 2, 4]

    x_val = 2
    y_val = lagrange_interpolation(x_data, y_data, x_val)
    
    print(f"Interpolated value at x = {x_val}: {y_val:.4f}")