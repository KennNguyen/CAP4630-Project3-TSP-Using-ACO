# Travelling Salesman Problem Solution via Ant Colony Optimization

In this project, swarm intelligence aka Ant Colony Optimization algorithm is used to solve the Travelling Salesman Problem.

## Project Overview 
$$\textbf{Ant Colony Optimization}$$ 
Ant Colony Optimization is a probabilistic technique for finding optimal paths. The creator of this algorithm technique, Marco Dorigo, based this algorithm off of foraging behavior of an ant for seeking a path between their colony and a food source. This is done by their use of pheromones left behind on their trails to the food source. These pheromones can be almost be thought of as weights on an edge of a graph. With this description, it can be seen that this optimization algorithm is part of the Ant Colony algorithms family which is also part of Swarm Intelligence method as well as make up a portion of the metaheuristic optimizations.  

$$\textbf{Edge Selection Formula}$$
![Edge Selection Formula](https://raw.githubusercontent.com/KennNguyen/CAP4630-Project3-TSP-Using-ACO/main/images/ESF.png)
LHS: The probability of ant 'k' will move from city 'x' to city 'y.'
RHS: The pheromone level on the path from city 'x' to city 'y' times the attractiveness of the path from city 'x' to city 'y' divided by the sum over all cities 'z' that are allowed to be visited from city 'y'. The denominator normalizes the probability so that the sum of probabilities of moving from city 'x' to all allowed cities 'y' is 1.
Parameters: 'a' and 'b' control the relative importance of the pheromone level and the attractiveness, respectively.

$$\textbf{Pheromone Update Rule Formula}$$
$$\tau_{xy}\leftarrow(1-\rho)\tau_{xy}\;+\;\sum_{k}\Delta\tau^{k}_{xy}$$
LHS: The amount of pheromone on an edge on that given x-coordinate and y-coordinate.
RHS: $\rho$ represents rate of pheromone evaporation. So given the rate of pheromone evaporation multiplied by the amount of pheromone on that given edge with the addition of the amount of pheromone left on that edge represented by $\Delta\tau^{k}_{xy}$.

$$\textbf{Pheromone Deposit Calculation in Ant Colony Optimization}$$
$$\Delta\tau^{k}_{xy}\;=\;\begin{cases}\frac{Q}{L_{k}}\;if\;ant\;k\;uses\;edge\;xy\;in\;its\;tour\\0\;\;\;\;\;\;\;\;otherwise\end{cases}$$
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
