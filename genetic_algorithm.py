import random

def calculate_fitness(ind, prices, weights, capacity):
  sum_of_prices = 0
  sum_of_weights = 0
  for i in range(len(ind)):
    if ind[i] == 1.0:
      sum_of_prices += prices[i]
      sum_of_weights += weights[i]
  fitness = sum_of_prices if sum_of_weights <= capacity else 0.0
  return fitness

def crossover(parent1, parent2, cross_rate):
  # decide if two parents will crossover their gene based on crossover rate
  if random.random() < cross_rate:
    # select a random index (gene) and swap every gene starting from that index
    split_point = random.randint(0, len(parent1)-1)

    # split excludes split point index
    parent1_start = parent1[:split_point]
    # includes split point index
    parent1_end = parent1[split_point:]

    # split excludes split point index
    parent2_start = parent2[:split_point]
    # includes split point index
    parent2_end = parent2[split_point:]

    # append each end to the other parent's start
    child1 = parent1_start + parent2_end
    child2 = parent2_start + parent1_end
  else:
    # pass down exact copies of their gene
    child1 = parent1
    child2 = parent2
  return child1, child2

def mutation(child, mut_rate):
  # decide if child will mutate based on mutation rate
  if random.random() < mut_rate:
    # swap two random indexes
    i = random.randint(0, len(child)-1)
    j = random.randint(0, len(child)-1)
    temp = child[i]
    child[i] = child[j]
    child[j] = temp
  return child

def genetic_algorithm(data, population_size, num_generations, mut_rate, cross_rate, tournament_size):
  weights = data.Weights
  prices = data.Prices
  capacity = data.Capacity
  n = len(prices)

  population = []

  for i in range(population_size):
    # initialize as combination that is most likely over capacity
    solution = [1.0] * n
    # make random combinations
    for j in range(n):
      solution[j] = float(random.randint(0,1))
    # add solution to population
    population.append(solution)

  # for the number of generations
  for k in range(num_generations):
    # until we have enough fit individuals for next generation (original population size)
    new_population = []
    for l in range(population_size):
      tournament = random.choices(population, k=tournament_size)
      # choose best individual based on probability p = 1
      best_individual = tournament[0]
      best_tournament_fitness = 0.0
      for individual in tournament:
        fitness = calculate_fitness(individual, prices, weights, capacity)
        if fitness > best_tournament_fitness:
          best_individual = individual
          best_tournament_fitness = fitness
      # add tournament's champion to new population
      new_population.append(best_individual)
    population = new_population

    # individuals in new population will crossover genes pass down exact copies
    # for each individual in new population
    for individual in population:
      # find a random partner that's not itself
      partners = population.copy()
      partners.remove(individual)
      index = random.randint(0, len(partners)-1)
      partner = partners[index]
      child1, child2 = crossover(individual, partner, cross_rate)
      # remove parents from population
      population.remove(individual)
      population.remove(partner)
      # add children after mutating
      population.append(mutation(child1, mut_rate))
      population.append(mutation(child2, mut_rate))
  # find solution with best fitness in final generation
  best_solution = []
  best_solution_price = 0.0
  for solution in population:
    fitness = calculate_fitness(solution, prices, weights, capacity)
    if fitness > best_solution_price:
      best_solution = solution
      best_solution_price = fitness
  return best_solution_price, best_solution
