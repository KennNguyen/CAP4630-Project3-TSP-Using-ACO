import random
import numpy as np
import matplotlib.pyplot as plt

# Initialize constants
N = 25
ITERATIONS = 100
ALPHA = 1
BETA = 5
EVAPORATION = 0.5
INITIAL_PHEROMONE = 1.0

# Initialize cities
random.seed(42)
cities = [(random.randint(0, 200), random.randint(0, 200)) for _ in range(N)]

# Initialize distances
distances = np.zeros((N, N))
for i in range(N):
  for j in range(N):
    x1, y1 = cities[i]
    x2, y2 = cities[j]
    distances[i][j] = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Initialize pheromones
pheromones = np.ones((N, N)) * INITIAL_PHEROMONE

# Ant class
class Ant:
  def __init__(self):
    self.route = random.sample(range(N), N)
    self.distance = 0.0

  def calculate_distance(self):
    self.distance = sum(distances[self.route[i-1]][self.route[i]] for i in range(N))

# Initialize ant population
ants = [Ant() for _ in range(N)]

# Main loop
best_route = []
best_distance = float('inf')

for iteration in range(ITERATIONS):
  # Ant logic
  for ant in ants:
    ant.calculate_distance()
    if ant.distance < best_distance:
      best_distance = ant.distance
      best_route = ant.route[:]

  # Pheromone update
  for i in range(N):
    for j in range(N):
      pheromones[i][j] *= EVAPORATION

  for ant in ants:
    for i in range(N - 1):
      pheromones[ant.route[i]][ant.route[i+1]] += 1 / ant.distance

# Print and plot the result
print("Best Route:", best_route)
print("Best Distance:", best_distance)

x_coords = [cities[i][0] for i in best_route]
y_coords = [cities[i][1] for i in best_route]
plt.plot(x_coords, y_coords, 'bo-')
plt.show()
