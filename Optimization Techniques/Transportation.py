from pulp import *

# Create the problem
prob = LpProblem("Transportation Problem", LpMinimize)

# Sources and their supply
sources = ["S1", "S2", "S3"]
supply = {"S1": 300, "S2": 400, "S3": 500}

# Destinations and their demand
destinations = ["D1", "D2", "D3", "D4"]
demand = {"D1": 250, "D2": 350, "D3": 400, "D4": 200}

# Cost matrix
costs = {
    "S1": {"D1": 3, "D2": 1, "D3": 7, "D4": 4},
    "S2": {"D1": 2, "D2": 6, "D3": 5, "D4": 9},
    "S3": {"D1": 8, "D2": 3, "D3": 3, "D4": 2}
}

# Create decision variables
routes = [(s, d) for s in sources for d in destinations]
vars = LpVariable.dicts("Route", (sources, destinations), 0, None, LpInteger)

# Add objective function
prob += lpSum([vars[s][d] * costs[s][d] for (s, d) in routes]), "Total Transportation Cost"

# Add supply constraints
for s in sources:
    prob += lpSum([vars[s][d] for d in destinations]) <= supply[s], f"Total_out_{s}"

# Add demand constraints
for d in destinations:
    prob += lpSum([vars[s][d] for s in sources]) >= demand[d], f"Total_in_{d}"

# Solve the problem
prob.solve()

# Print the results
print(f"Status: {LpStatus[prob.status]}")
print(f"Total Cost: ${value(prob.objective):,.2f}\n")

# Print the solution
print("Optimal Transportation Plan:")
for s in sources:
    for d in destinations:
        if vars[s][d].varValue > 0:
            print(f"Ship {vars[s][d].varValue} units from {s} to {d}")