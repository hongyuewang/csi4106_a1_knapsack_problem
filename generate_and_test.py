def gen_and_test(data):

  return best_solution_price, best_solution


def run():
    solutions = []
    for _, row in dataset.iterrows():
        target = row['Best price']
        solution, indexes = gen_and_test(row)
        solutions.append(1 if target == solution else 0)
    
    # Accuracy
    print('Accuracy of best prices found is', np.mean(solutions))
