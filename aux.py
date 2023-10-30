from typing import Optional
import genetic_tsp
import random
from matplotlib import pyplot as plt

Point = tuple[float, float]

def calculate_distance(point1: Point, point2: Point) -> float:
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def ask_yes_no_question(question: str, default: bool = False) -> bool:
    """Asks a yes or no question and returns a boolean"""
    while True:
        print(question + " (y/n)", end = " ")
        userInput = input()

        if (len(userInput) == 0 and default):
            return default
        elif userInput.lower() == "y":
            return True
        elif userInput.lower() == "n":
            return False

def query_user(query: str, default: Optional[str] = None) -> str:
    """Queries the user for input and returns their response"""
    if default is not None:
        print(f"{query} [default={default}]", end = " ")
    else:
        print(query, end = " ")

    user_input = input()
    user_did_not_input_anything = len(user_input) == 0

    if default is not None and user_did_not_input_anything:
        return default
    elif not user_did_not_input_anything:
        return user_input

    return query_user(query, default)

def hash_city_name(n: int) -> str:
    name = ""

    while n >= 0:
        name = chr(65 + (n % 26)) + name
        n = n // 26 - 1

    return name

def print_cities(cities: list[genetic_tsp.City]) -> None:
    print("{:6}\t{:>6}\t{:>6}".format("City", "X", "Y"))

    for city in cities:
        print("{:6}\t{:>6.2f}\t{:>6.2f}".format(city[0],city[1],city[2]))

def generate_random_cities(count: int) -> list[genetic_tsp.City]:
    """Returns initialized list of random cities."""
    cities: list[genetic_tsp.City] = []
    max_x_axis = 200
    max_y_axis = 200

    for i in range(count):
        city_name = hash_city_name(i)
        x = random.uniform(0, max_x_axis)
        y = random.uniform(0, max_y_axis)
        cities.append((city_name, x, y))

    return cities

def plot_route(route: genetic_tsp.Route) -> None:
    x = [point[1] for point in route]
    y = [point[2] for point in route]

    plt.scatter(x, y, color="red", label="Cities")
    plt.plot(x + [x[0]], y + [y[0]], color="blue", linestyle="dashed", linewidth=1)

def plot_cities(cities: list[genetic_tsp.City]) -> None:
    x = [city[1] for city in cities]
    y = [city[2] for city in cities]

    plt.scatter(x, y, color="red", label="Cities")
