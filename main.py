import pandas as pd
import itertools
import numpy as np

import utils

from generate_and_test import gen_and_test
from greedy_search import greedy
from simulated_annealing import simulated_annealing
from genetic_algorithm import genetic_algorithm

url = "https://raw.githubusercontent.com/hongyuewang/csi4106_a1_knapsack_problem/main/knapsack_5_items.csv"

dataset = pd.read_csv(url)

print(dataset.columns)
print(dataset.head(10))

dataset = dataset.dropna()
string_to_list = utils.string_to_list

dataset.Weights = dataset.Weights.apply(lambda x : string_to_list(x))
dataset.Prices = dataset.Prices.apply(lambda x : string_to_list(x))
dataset['Best picks'] = dataset['Best picks'].apply(lambda x : string_to_list(x))

def generate_and_test_run():
    solutions = []
    for _, row in dataset.iterrows():
        target = row['Best price']
        solution, indexes = gen_and_test(row)
        solutions.append(1 if target == solution else 0)
    # Accuracy
    print('Accuracy of best prices found is', np.mean(solutions))
    print("The number of optimal solutions found is", len(list(filter(lambda x:x > 0 ,solutions))))

def greedy_search_run():
    solutions_greedy = []
    for _, row in dataset.iterrows():
        target = row['Best price']
        solution, indexes = greedy(row)
        solutions_greedy.append(1 if target == solution else 0)

    print("Greedy Accuracy is", np.mean(solutions_greedy))
    print("The number of optimal solutions found is", len(list(filter(lambda x:x > 0 ,solutions_greedy))))

def simulated_annealing_run():
    solutions_sa = []
    for _, row in dataset.iterrows():
        target = row['Best price']
        solution, indexes = simulated_annealing(row, N = 10, initial_temperature=1, cooling_rate=0.95)
        solutions_sa.append(1 if target == solution else 0)

    print("Simulated Annealing Accuracy is", np.mean(solutions_sa))
    print("The number of optimal solutions found is", len(list(filter(lambda x:x > 0 ,solutions_sa))))

def genetic_algorithm_run():
    solutions_ga = []
    for _, row in dataset.iterrows():
        target = row['Best price']
        solution, indexes = genetic_algorithm(row, population_size = 50, num_generations = 50, mut_rate = 0.1, cross_rate = 0.7, tournament_size = 5)
        solutions_ga.append(1 if target == solution else 0)
    
    print("Genetic Algorithm Accuracy is", np.mean(solutions_ga))
    print("The number of optimal solutions found is", len(list(filter(lambda x:x > 0 ,solutions_ga))))

generate_and_test_run()
greedy_search_run()
simulated_annealing_run()
genetic_algorithm_run()
