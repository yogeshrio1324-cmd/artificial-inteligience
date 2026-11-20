
# Genetic Algorithm for Function Optimization

import random

# Define the fitness function
# Function: f(x) = x^2
def fitness(x):
    return x * x

# Generate initial population
population = [random.uniform(0, 10) for _ in range(10)]

# Genetic Algorithm parameters
generations = 50
mutation_rate = 0.1

# Genetic Algorithm
for generation in range(generations):

    # Evaluate fitness
    population = sorted(
        population,
        key=fitness,
        reverse=True
    )

    # Select best individuals
    new_population = population[:2]

    # Generate new population
    while len(new_population) < 10:

        # Crossover
        parent1 = random.choice(population[:5])
        parent2 = random.choice(population[:5])

        child = (parent1 + parent2) / 2

        # Mutation
        if random.random() < mutation_rate:
            child += random.uniform(-1, 1)

        # Keep values within range
        child = max(0, min(10, child))

        new_population.append(child)

    population = new_population

# Find best solution
best_solution = max(population, key=fitness)

print("Best Solution (x):", best_solution)
print("Maximum Fitness Value:", fitness(best_solution))
print("Number of Generations:", generations)
