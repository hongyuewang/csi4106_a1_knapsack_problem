def greedy(data):

  return best_solution_price, best_solution

def run():
    solutions_greedy = []
    for _, row in dataset.iterrows():
        target = row['Best price']
        solution, indexes = greedy(row)
        solutions_greedy.append(1 if target == solution else 0)

    print("Greedy Accuracy is", np.mean(solutions_greedy))
