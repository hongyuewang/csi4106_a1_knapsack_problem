import random
import math


def simulated_annealing(data, N, initial_temperature, cooling_rate):



  return best_solution_price, best_solution

def run():
    solutions_sa = []
    for _, row in dataset.iterrows():
        target = row['Best price']
        solution, indexes = simulated_annealing(row, N = 10, initial_temperature=1, cooling_rate=0.95)
        solutions_sa.append(1 if target == solution else 0)

    print("Simulated Annealing Accuracy is", np.mean(solutions_sa))

