import itertools

def gen_and_test(data):
  weights = data.Weights
  prices = data.Prices
  capacity = data.Capacity
  best_solution_price = 0.0
  best_solution = []

  # generate all possisble 2^5 (32) combinations using itertools
  n = len(weights)
  # for every combination from 1 to 5
  for l in range(1, n+1):
    # for every combination of length l of object indexes 0-4
    for combination in itertools.combinations(range(n), l):
      weight = sum(weights[i] for i in combination)
      price = sum(prices[i] for i in combination)
      # check if weight is under within the knapc=sack's capacity and if the price is the highest so far
      # if true, set this combination as current best
      if weight <= capacity and price > best_solution_price:
        best_solution_price = price
        best_solution = combination

  return best_solution_price, best_solution
