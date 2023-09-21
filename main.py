import pandas as pd
import itertools
import numpy as np

import utils

from generate_and_test import gen_and_test
import greedy_search
import simulated_annealing
import genetic_algorithm

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

generate_and_test_run()
#greedy_search.run()
#simulated_annealing.run()
#genetic_algorithm.run()
