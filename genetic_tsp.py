import random
import aux
from matplotlib import pyplot as plt

City = tuple[str, float, float]
Route = list[City]
Population = list[Route]

# Step 1: Generate a random population of `n` individuals.
def generate_random_population(size: int, city_count: int) -> Population:
    population: Population = []

    for _ in range(size):
        cities = aux.generate_random_cities(city_count)

        aux.plot_cities(cities)
        random.shuffle(cities)
        population.append(cities)

    return population

# Step 2: Calculate the fitness of each individual in the population.
def calculate_fitness(route: Route) -> float:
    total_distance = 0.0
    previous_city = None

    for city in route:
        if previous_city is not None:
            total_distance += aux.calculate_distance((previous_city[1], previous_city[2]), (city[1], city[2]))

        previous_city = city

    return total_distance

# Step 3: Select the best-fit `k` individuals for reproduction.
def select_parents(population: Population, k: int) -> Population:
    # Sort the population by fitness (ascending, prioritizing shortest distance first).
    sorted_population = sorted(population, key=calculate_fitness, reverse=False)

    return sorted_population[:k]

# Step 4: Create `n` new individuals by combining the best `k` individuals.
def crossover(parent_a: Route, parent_b: Route) -> Route:
    idx1, idx2 = sorted(random.sample(range(len(parent_a)), 2))
    common = parent_a[idx1:idx2]
    child = [city for city in parent_b if city not in common]

    child[idx1:idx1] = common

    return child

# Step 5: Mutate the new individuals.
def mutate(route: Route, mutation_rate: float) -> Route:
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]

    return route

# Step 6: Main loop.
def run(population: Population, k: int, iterations: int, mutation_rate: float) -> Population:
    evolved_population = population[:]

    for _ in range(iterations):
        parents = select_parents(evolved_population, k)
        new_population: Population = []

        while len(new_population) < population_size:
            parent_a, parent_b = random.sample(parents, 2)
            child = crossover(parent_a, parent_b)
            mutated_child = mutate(child, mutation_rate)

            new_population.append(mutated_child)

        evolved_population = new_population

    return evolved_population

def initialize_and_plot(
    iterations: int,
    population_size: int,
    k: int,
    mutation_rate: float,
    city_count: int
) -> None:
    PLOT_STEP_DELAY = 0.01

    best_route = None
    best_distance = float("inf")

    # Prepare the graph. Reuse a single figure for all plots.
    plt.figure()

    population = generate_random_population(population_size, city_count)

    for i in range(iterations):
        # Get the best individual in the current population
        population = run(population, k, 1, mutation_rate)
        best_current_route = select_parents(population, 1)[0]
        best_current_distance = calculate_fitness(best_current_route)

        if best_current_distance < best_distance:
            best_distance = best_current_distance
            best_route = best_current_route

        # Plot the current best route.
        plt.title(f"Iteration {i+1}, Distance: {best_current_distance:.2f}, Best distance: {best_distance:.2f}")
        plt.xlabel("X")
        plt.ylabel("Y")
        aux.plot_route(best_current_route)
        plt.show(block=False)

        # Pause for brief moment to allow update to be seen.
        plt.pause(PLOT_STEP_DELAY)

        # Clear the plot for the next iteration.
        plt.clf()

    assert best_route is not None, "a best route should always be found"
    print("Genetic Algorithm finished.")
    print(f"Best distance: {best_distance:.2f}")
    print(f"Best route: {best_route}")

if __name__ == "__main__":
    print("Welcome to a Genetic Algorithm solver for  the TSP!")

    iterations = int(aux.query_user("How many iterations?", "1000"))
    city_count = int(aux.query_user("How many cities?", "20"))
    mutation_rate = float(aux.query_user("What mutation rate (float)?", "0.1"))
    population_size = int(aux.query_user("What population size?", "50"))
    k = int(aux.query_user("What k value?", "3"))
    seed = aux.query_user("What random seed?", "123456")

    random.seed(seed)
    initialize_and_plot(iterations, population_size, k, mutation_rate, city_count)
