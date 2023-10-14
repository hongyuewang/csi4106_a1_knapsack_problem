import random
import math

def sum_of_prices(solution, prices):
  sum = 0
  for i in range(len(solution)):
    if solution[i] == 1.0:
      sum += prices[i]
  return sum

def sum_of_weights(solution, weights):
  sum = 0
  for i in range(len(solution)):
    if solution[i] == 1:
      sum += weights[i]
  return sum

def accept(delta_energy, temperature):
  # we want to maximize energy (price), therefore we want energy change to be positive
  if delta_energy > 0:
    return True
  else:
    r = random.random()
    # we do not negate the exponent since delta is already negative, a positive exponent would always be bigger than r, which we do not want
    if r < math.exp(delta_energy/temperature):
      return True
    else:
      return False

def simulated_annealing(data, N, initial_temperature, cooling_rate):
  weights = data.Weights
  prices = data.Prices
  capacity = data.Capacity

  temperature = initial_temperature
  
  n = len(prices)
  # initialize as combination that is most likely over capacity
  best_solution = [1.0] * n
  # make random combinations until we find a valid solution
  while(sum_of_weights(best_solution, weights) > capacity):
    for i in range(n):
      best_solution[i] = float(random.randint(0,1))
  
  # energy/fitness is the prices of objects in the knapsack
  energy = sum_of_prices(best_solution, prices)

  # set minimum temperature to a value close to 0, a true 0 cooldown would take too long.
  minimum_temperature = 0.05
  maximum_energy = sum(prices)

  while(temperature > minimum_temperature and energy < maximum_energy):
    # N is the number of iterations per temperature
    for i in range(N):
      # copy current best solution
      new_solution = best_solution
      # flip a random index for neighbouring solution
      j = random.randint(0, len(prices) - 1)
      new_solution[j] = 1 - new_solution[j]
      # if exceeds capacity, energy is 0
      if sum_of_weights(new_solution, weights) > capacity:
        new_energy = 0.0
      else:
        # otherwise, it is also the sum of the objects' values
        new_energy = sum_of_prices(new_solution, prices)
      # difference in the new solution and current best solution's energies
      delta_energy = new_energy - energy
      # run acceptance function, if True, set new solution as best solution
      if accept(delta_energy, temperature):
        best_solution = new_solution
        energy = new_energy
    # lower temperature after N iterations
    temperature = cooling_rate * temperature
  # after finding the best solution, set the price as the energy
  best_solution_price = energy
  return best_solution_price, best_solution
