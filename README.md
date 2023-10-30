# Traveling Salesman Problem Solution via Ant Colony Optimization

In this project, swarm intelligence aka Ant Colony Optimization algorithm is used to solve the Traveling Salesman Problem.

## Authors

* **[Kenneth Nguyen](https://github.com/KennNguyen/)** (Reporter)
* **[Zee Fisher](https://github.com/zmfisher01)** (Architect)
* **[Yurixander R.](https://github.com/yurixander)** (Developer)

## Project Overview
$$\textbf{Ant Colony Optimization}$$
Ant Colony Optimization is a probabilistic technique for finding optimal paths. The creator of this algorithm technique, Marco Dorigo, based this algorithm off of foraging behavior of an ant for seeking a path between their colony and a food source. This is done by their use of pheromones left behind on their trails to the food source. These pheromones can be almost be thought of as weights on an edge of a graph. With this description, it can be seen that this optimization algorithm is part of the Ant Colony algorithms family which is also part of Swarm Intelligence method as well as make up a portion of the metaheuristic optimizations.

$$\textbf{Edge Selection Formula}$$

![Edge Selection Formula](https://raw.githubusercontent.com/KennNguyen/CAP4630-Project3-TSP-Using-ACO/main/images/ESF.PNG)

LHS: The probability of ant 'k' will move from city 'x' to city 'y.'
RHS: The pheromone level on the path from city 'x' to city 'y' times the attractiveness of the path from city 'x' to city 'y' divided by the sum over all cities 'z' that are allowed to be visited from city 'y'. The denominator normalizes the probability so that the sum of probabilities of moving from city 'x' to all allowed cities 'y' is 1.
Parameters: 'a' and 'b' control the relative importance of the pheromone level and the attractiveness, respectively.

$$\textbf{Pheromone Update Rule Formula}$$

![Edge Selection Formula](https://raw.githubusercontent.com/KennNguyen/CAP4630-Project3-TSP-Using-ACO/main/images/PDF.PNG)

LHS: The amount of pheromone on an edge on that given x-coordinate and y-coordinate.
RHS: $\rho$ represents rate of pheromone evaporation. So given the rate of pheromone evaporation multiplied by the amount of pheromone on that given edge with the addition of the amount of pheromone left on that edge represented by $\Delta\tau^{k}_{xy}$.

$$\textbf{Pheromone Deposit Calculation in Ant Colony Optimization}$$

![Edge Selection Formula](https://raw.githubusercontent.com/KennNguyen/CAP4630-Project3-TSP-Using-ACO/main/images/PUR.PNG)

LHS: The change in amount of pheromone left on that edge on that given x-coordinate and y-coordinate.
RHS: Q is the pheromone deposit factor divided by L is the cost of the ant tour length.

$$\textbf{Implementation}$$
```
	Begin
		Initialize
		While stopping criterion not satisfied do
			Position each ant in a starting node
			Repeat
				For each ant do
					Choose next node by applying state transition rule
					Apply step by step pheromone update
				End For
			Until every ant has built a solution
			Update best solution
			Apply offline pheromone update
		End While
	End
```

$$\textbf{Report}$$

Team : Yurixander Ricardo Silva, Zee Fisher, Kenneth Nguyen

With our knowledge of the travelling salesman problem with genetic algorithm, we were able to have a better grasp of the problem and its requirement and restraints. For example, we understood that visiting each node exactly once to minimize the total distance travelled. Moreover, we were able to reuse the encoding due to it being the same problem. In addition, with the experience from genetic algorithm, we were able to approach parameter tuning for ant colony optimization on better grounds. Furthermore, with experimentation in the genetic algorithm, we were able to use the same methodology when evaluating the ant colony optimization's performance.

How were the cities and distances represented (as a data structure)? : Cities are represented as tuples in which it contains 'x' and 'y' coordinates of the cities, while the Euclidean distance is contained in a 2D array.
How did you encode the solution space? : Each of the ant's routes is encoded in a list on indices in the order of the cities visited.
How did you handle the creation of the initial ant population? : The initial population of the ants was created by instantiating 'N' Ant objects.
How did you handle the updating of the pheromone trails? : After each iteration, the pheromones levels on all edges evaporates by multiplying with the evaporation rate and then the ants deposits pheromones on the edge its traversing with the amount that is inversely proportional to the distance of its route.
Which strategy(ies) did you use to compute the best solution? : The best solution is computed by having the distance be updated with the shortest distance recorded when the ant completes its route.
Which stopping condition did you use? Why? : The stopping condition we went with is to have it run a fixed number of iterations due to simplicity and predictability on the runtime. 
What other parameters, design choices, initialization and configuration steps are relevant to your design and implementation? : The implementation of parameters 'A' and 'B' to control the influence of the pheromone level and the use of inverse distance for the probability of selecting the next city.
Which (simple) experiments have you run to observe the impact of different design decisions and parameter values? Post their results and your comments.
