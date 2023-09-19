import random

def calculate_fitness(ind, prices, weights, capacity):


  return fitness

def crossover(parent1, parent2, cross_rate):


  return child1, child2

def mutation(child, mut_rate):


  return child

def genetic_algorithm(data, population_size, num_generations, mut_rate, cross_rate, tournament_size):


  return best_solution_price, best_solution

def run():
    solutions_ga = []
    for _, row in dataset.iterrows():
        target = row['Best price']
        solution, indexes = genetic_algorithm(row, population_size = 50, num_generations = 50, mut_rate = 0.1, cross_rate = 0.7, tournament_size = 5)
        solutions_ga.append(1 if target == solution else 0)
    
    print("Genetic Algorithm Accuracy is", np.mean(solutions_ga))

