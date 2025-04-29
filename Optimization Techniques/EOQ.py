import math

def get_positive_input(prompt, input_type=float):
    """Get positive numerical input from user"""
    while True:
        try:
            value = input_type(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_eoq(demand, ordering_cost, holding_cost):
    """Calculate Economic Order Quantity"""
    return math.sqrt((2 * demand * ordering_cost) / holding_cost)

def calculate_total_cost(demand, ordering_cost, holding_cost, order_quantity):
    """Calculate total inventory cost"""
    ordering_cost_total = (demand / order_quantity) * ordering_cost
    holding_cost_total = (order_quantity / 2) * holding_cost
    return ordering_cost_total + holding_cost_total

def main():
    print("=== Economic Order Quantity (EOQ) Calculator ===")
    
    # Get user inputs
    annual_demand = get_positive_input("Enter annual demand (units): ")
    order_cost = get_positive_input("Enter ordering cost per order ($): ")
    holding_cost = get_positive_input("Enter holding cost per unit per year ($): ")
    
    # Calculate EOQ
    eoq = calculate_eoq(annual_demand, order_cost, holding_cost)
    print(f"\nEconomic Order Quantity: {eoq:.2f} units")
    
    # Calculate costs at EOQ
    total_cost = calculate_total_cost(annual_demand, order_cost, holding_cost, eoq)
    ordering_cost = (annual_demand / eoq) * order_cost
    holding_cost_total = (eoq / 2) * holding_cost
    
    print("\nCost Analysis at EOQ:")
    print(f"- Ordering Cost: ${ordering_cost:.2f}")
    print(f"- Holding Cost: ${holding_cost_total:.2f}")
    print(f"- TOTAL COST: ${total_cost:.2f}")
    
    # Compare with user-specified order quantity
    compare = input("\nWould you like to compare with another order quantity? (y/n): ").lower()
    if compare == 'y':
        while True:
            try:
                user_qty = float(input("Enter order quantity to compare: "))
                if user_qty <= 0:
                    print("Please enter a positive value.")
                    continue
                
                user_total = calculate_total_cost(annual_demand, order_cost, holding_cost, user_qty)
                print(f"\nComparison with {user_qty:.2f} units order:")
                print(f"- Total Cost: ${user_total:.2f}")
                print(f"- Difference from EOQ: ${user_total - total_cost:.2f}")
                
                if user_qty < eoq:
                    print("(This order quantity is smaller than EOQ - more frequent ordering)")
                elif user_qty > eoq:
                    print("(This order quantity is larger than EOQ - less frequent ordering)")
                
                another = input("\nCompare another quantity? (y/n): ").lower()
                if another != 'y':
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    print("\nThank you for using the EOQ Calculator!")

if __name__ == "__main__":
    main()