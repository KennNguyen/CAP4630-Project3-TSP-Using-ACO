import random
import aux
from matplotlib import pyplot as plt

City = tuple[str, float, float] # name, x, y 
Edge = tuple[City, City, int] # Connection between 2 cities and its pheremones
Route = list[City]


#  Main loop.
#def run(population: Population, k: int, iterations: int, mutation_rate: float) -> Population:

def initialize_and_plot(
    iterations: int,
    population_size: int,
    city_count: int
) -> None:
    PLOT_STEP_DELAY = 0.01

    best_route = None
    best_distance = float("inf")

    # Prepare the graph. Reuse a single figure for all plots.
    plt.figure()


    for i in range(iterations):

        # Plot the current best route.
        #plt.title(f"Iteration {i+1}, Distance: {best_current_distance:.2f}, Best distance: {best_distance:.2f}")
        plt.title("Test")
        plt.xlabel("X")
        plt.ylabel("Y")
        #aux.plot_route(best_current_route)
        plt.show(block=False)

        # Pause for brief moment to allow update to be seen.
        plt.pause(PLOT_STEP_DELAY)

        # Clear the plot for the next iteration.
        plt.clf()

    assert best_route is not None, "a best route should always be found"
    print("Algorithm finished.")
    #print(f"Best distance: {best_distance:.2f}")
    #print(f"Best route: {best_route}")

if __name__ == "__main__":
    print("Welcome to a ACO solver for  the TSP!")

    iterations = int(aux.query_user("How many iterations?", "1000"))
    city_count = int(aux.query_user("How many cities?", "20"))
    population_size = int(aux.query_user("How many ants?", "50"))
    seed = aux.query_user("What random seed?", "123456")

    random.seed(seed)
    initialize_and_plot(iterations, population_size, city_count)
