import itertools

def gen_and_test(data):
  weights = data.Weights
  prices = data.Prices
  capacity = data.Capacity
  n = len(weights)
  best_solution_price = 0.0
  # initialize best solution as empty knapsack
  best_solution = [0.0] * n

  # generate all possible 2^5 (32) combinations using itertools
  # for every combination from 1 to 5
  for l in range(1, n+1):
    # for every combination of length l of object indexes 0-4
    for combination in itertools.combinations(range(n), l):
      weight = sum(weights[i] for i in combination)
      price = sum(prices[i] for i in combination)
      # check if weight is under within the knapcsack's capacity and if the price is the highest so far
      # if true, set this combination as current best
      if weight <= capacity and price > best_solution_price:
        best_solution_price = price
        # set every index present in combination to 1 in solution list
        for index in combination:
          best_solution[index] = 1.0

  return best_solution_price, best_solution
