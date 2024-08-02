import csv
import time
from itertools import combinations

BUDGET = 500
FILE_PATH = "data/actions_test.csv"


def load_database(file_path=FILE_PATH):
    """Load actions from database."""
    actions_list = []

    with open(file_path, "r") as csv_file:
        csv_actions = csv.DictReader(csv_file)
        for action in csv_actions:
            action['price'] = float(action['price'])
            action['profit'] = float(action['profit'])
            actions_list.append(action)

    return actions_list


def generate_combinations(actions_list):
    """Generate a list of possible combinations."""
    combinations_list = [[]]
    for action in actions_list:
        new_combinations = []
        for current_combination in combinations_list:
            new_combination = current_combination + [action]
            new_combinations.append(new_combination)
        combinations_list.extend(new_combinations)
    return combinations_list


def bruteforce_investment(actions_combinations, budget=BUDGET):
    """Calculate investement with a list of combinations without itertools."""
    max_profit = 0
    best_combination = None

    for combination in actions_combinations:
        total_cost = 0
        for action in combination:
            total_cost += action["price"]

        if total_cost <= budget:
            total_profit = 0
            for action in combination:
                total_profit += action["price"] * (action["profit"] / 100)

            if total_profit > max_profit:
                max_profit = total_profit
                best_combination = combination
    best_combination_names = [action["name"] for action in best_combination]
    print("Meilleur combinaison:")
    print(best_combination_names)
    print()
    print(f"Profit: {max_profit:.2f}€")


def bruteforce_investment_itertools(actions_list, budget=BUDGET):
    """Use of combinations from itertools to generate actions combinations."""
    max_profit = 0
    best_combination = None

    # Check all combinations of different sizes
    for r in range(1, len(actions_list) + 1):
        for combination in combinations(actions_list, r):
            total_cost = sum(action['price'] for action in combination)
            if total_cost <= budget:
                total_profit = sum(action['price'] * (action['profit'] / 100) for action in combination)
                if total_profit > max_profit:
                    max_profit = total_profit
                    best_combination = combination

    best_combination_names = [action["name"] for action in best_combination]
    print("Meilleure combinaison:")
    print(best_combination_names)
    print()
    print(f"Profit: {max_profit:.2f}€")


# Load datas.
actions_list = load_database()


# Bruteforce without itertols.
start_time = time.time()
actions_combinations = generate_combinations(actions_list)
bruteforce_investment(actions_combinations)
end_time = time.time()
print(f"Temps d'exécution sans itertools: {end_time - start_time:.4f} secondes\n")

# Bruteforce with itertools.
start_time = time.time()
bruteforce_investment_itertools(actions_list)
end_time = time.time()
print(f"Temps d'exécution avec itertools: {end_time - start_time:.4f} secondes")


# Méthode sans itertools (génération manuelle):
# Complexité temporelle : O((2^n)*k)
# Complexité spatiale : O(2n)

# Méthode avec itertools:
# Complexité temporelle : O((2^n)*k)
# Complexité spatiale : O(n)
