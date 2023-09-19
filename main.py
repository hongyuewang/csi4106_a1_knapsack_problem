import pandas as pd
import itertools
import numpy as np

import utils

import generate_and_test
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

generate_and_test.run()
greedy_search.run()
simulated_annealing.run()
genetic_algorithm.run()
