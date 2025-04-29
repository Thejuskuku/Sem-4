import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_assignment(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.
    
    Parameters:
    cost_matrix : 2D array
        Cost matrix where cost_matrix[i][j] represents the cost of assigning agent i to task j.
        
    Returns:
    row_ind, col_ind : array
        Optimal assignment of rows to columns that minimizes total cost.
    total_cost : float
        The total cost of the optimal assignment.
    """
    # Convert to numpy array if it's not already
    cost_matrix = np.array(cost_matrix)
    
    # Apply the Hungarian algorithm to find the optimal assignment
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    # Calculate the total cost of the optimal assignment
    total_cost = cost_matrix[row_ind, col_ind].sum()
    
    return row_ind, col_ind, total_cost

# Example usage:
if __name__ == "__main__":
    # Example cost matrix (3 agents x 3 tasks)
    cost_matrix = [
        [15, 40, 45],
        [20, 60, 35],
        [20, 40, 25]
    ]
    
    row_ind, col_ind, total_cost = solve_assignment(cost_matrix)
    
    print("Optimal assignments:")
    for agent, task in zip(row_ind, col_ind):
        print(f"Agent {agent+1} -> Task {task+1} (Cost: {cost_matrix[agent][task]})")
    
    print(f"\nTotal minimum cost: {total_cost}")