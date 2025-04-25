def newton_forward_interpolation(x, y, x_val):

    n = len(x)
    h = x[1] - x[0] 
    
    diff_table = [[0] * n for _ in range(n)]
    for i in range(n):
        diff_table[i][0] = y[i]
    
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i+1][j-1] - diff_table[i][j-1]
    
    u = (x_val - x[0]) / h
    
    result = diff_table[0][0]
    product_term = 1
    
    for i in range(1, n):
        product_term *= (u - (i - 1)) / i
        result += product_term * diff_table[0][i]
    
    return result

if __name__ == "__main__":

    x = [0, 1, 2, 3, 4]
    y = [1, 2, 4, 8, 16]
    
    x_val = 1.5

    y_val = newton_forward_interpolation(x, y, x_val)
    
    print(f"Interpolated value at x = {x_val}: {y_val:.4f}")
