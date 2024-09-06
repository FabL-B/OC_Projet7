import csv
import time
import tracemalloc

BUDGET = 500
FILE_PATH = "data/dataset1.csv"

def read_data_from_csv(file_path):
    """Reads action data from a CSV file and prepares it for processing."""
    action_data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            name = row['name']
            price = float(row['price']) * 100  # Convert price to cents (integer)
            profit_percentage = float(row['profit'])
            # Calculate real profit from percentage
            real_profit = price * (profit_percentage / 100)
            if price > 0:  # Only consider actions with a price greater than 0
                action_data.append((name, int(price), real_profit))  # Keep price as integer (cents)
    return action_data

def initialize_matrix(budget, num_actions):
    """Initialize the dynamic programming matrix with zeros."""
    return [[0 for _ in range(budget + 1)] for _ in range(num_actions + 1)]

def calculate_optimized_values(data, budget, matrix):
    """Fill the dynamic programming matrix with optimized values."""
    for i in range(1, len(data) + 1):
        name, action_cost, action_profit = data[i - 1]
        for current_budget in range(1, budget + 1):
            if action_cost <= current_budget:
                include_action = action_profit + matrix[i - 1][current_budget - action_cost]
                exclude_action = matrix[i - 1][current_budget]
                matrix[i][current_budget] = max(include_action, exclude_action)
            else:
                matrix[i][current_budget] = matrix[i - 1][current_budget]
    return matrix

def retrieve_selected_actions(data, matrix, budget):
    """Backtrack through the matrix to find which actions were selected."""
    selected_actions = []
    remaining_budget = budget
    num_actions = len(data)

    for i in range(num_actions, 0, -1):
        if matrix[i][remaining_budget] != matrix[i - 1][remaining_budget]:
            selected_action = data[i - 1]
            selected_actions.append(selected_action)
            remaining_budget -= selected_action[1]

    return selected_actions

def knapsack_solver(file_path=FILE_PATH, budget=BUDGET):
    """Run the knapsack problem solver to calculate the optimal strategy."""
    # Convert the budget to cents as profits are converted to cents
    budget = budget * 100
    data = read_data_from_csv(file_path)
    matrix = initialize_matrix(budget, len(data))
    matrix = calculate_optimized_values(data, budget, matrix)
    selected_actions = retrieve_selected_actions(data, matrix, budget)
    max_profit = matrix[-1][-1]
    return matrix, max_profit, selected_actions

if __name__ == "__main__":

    # Start measuring memory usage
    tracemalloc.start()

    # Start measuring time
    start_time = time.time()

    # Run the knapsack solver
    matrix, max_profit, selected_actions = knapsack_solver()

    # Stop measuring time
    end_time = time.time()
    execution_time = end_time - start_time

    # Stop measuring memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Display results
    print(f"Maximum Profit: {max_profit / 100:.2f}")
    print("\nSelected Actions:")
    for action in selected_actions:
        print(f"Action: {action[0]}, Cost: {action[1] / 100:.2f}, Profit: {action[2] / 100:.2f}")

    # Display time and memory usage
    print(f"\nExecution time: {execution_time:.6f} seconds")
    print(f"\nMemory usage: {current / 1024:.6f} KB")
    print(f"\nPeak memory usage: {peak / 1024:.6f} KB")
