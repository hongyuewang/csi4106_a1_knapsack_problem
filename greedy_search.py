def greedy(data):
  weights = data.Weights
  prices = data.Prices
  capacity = data.Capacity
  best_solution_price = 0.0
  n = len(prices)
  # initialize best solution as empty knapsack
  best_solution = [0.0] * n

  # build a list of dictionaries with price, weight and index of each object
  object_info_list = []
  for i in range(n):
    object_info_list.append({'price': prices[i], 'weight': weights[i], 'index': i})

  # sort this by descending price first, then ascending weight for objects with same price
  object_info_list = list(reversed(sorted(object_info_list, key = lambda x: (x['price'], -x['weight']))))

  # for each object, starting with most valuable, check if weight fits within the remaining capacity
  for object in object_info_list:
    if object['weight'] <= capacity:
      best_solution[object['index']] = 1.0
      # reduce remaining capacity by the weight of newly added object
      capacity -= object['weight']
      # add object's price to total price
      best_solution_price += object['price']

  return best_solution_price, best_solution
