import numpy as np

def input_payoff_matrix():
    rows = int(input("Enter the number of rows in the payoff matrix: "))
    cols = int(input("Enter the number of columns in the payoff matrix: "))
    
    payoff_matrix = []
    for _ in range(rows):
        row = [int(x) for x in input().split()]
        payoff_matrix.append(row)
    
    return np.array(payoff_matrix)

def calculate_strategies(payoff_matrix):
    row_player_payoffs = np.min(payoff_matrix, axis=1)
    column_player_payoffs = -np.max(payoff_matrix, axis=0)
    
    strategy_a = row_player_payoffs / np.sum(row_player_payoffs)
    strategy_b = column_player_payoffs / np.sum(column_player_payoffs)
    
    return strategy_a, strategy_b

def calculate_payoffs(payoff_matrix, strategy_a, strategy_b):
    payoffs_a = np.dot(payoff_matrix, strategy_b)
    payoffs_b = np.dot(payoff_matrix.T, strategy_a)
    
    return payoffs_a, payoffs_b

def find_nash_equilibrium(strategy_a, strategy_b):
    return np.allclose(np.dot(strategy_a, strategy_b), 1.0)

def main():
    payoff_matrix = input_payoff_matrix()
    strategy_a, strategy_b = calculate_strategies(payoff_matrix)
    
    payoffs_a, payoffs_b = calculate_payoffs(payoff_matrix, strategy_a, strategy_b)
    print("Player A's Payoffs:", payoffs_a)
    print("Player B's Payoffs:", payoffs_b)
    
    if find_nash_equilibrium(strategy_a, strategy_b):
        print("Nash Equilibrium reached.")
    else:
        print("Nash Equilibrium not reached.")

if __name__ == "__main__":
    main()
