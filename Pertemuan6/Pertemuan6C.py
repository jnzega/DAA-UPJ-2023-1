import matplotlib
import matplotlib.pyplot as plt
import random
import time
import itertools

#Try All Tours (exact_TSP)
def exact_TSP(cities):
    "Generate all possible tours of the cities and choos the shortest one."
    return shortest(alltours(cities))

def shortest(tours):
    "return the tour with the minimum total distance."
    return min(tours, key=total_distance)

#Representing tours
alltours = itertools.permutations

cities = {1, 2, 3}

list(alltours(cities))

[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3,1,2), (3, 2, 1)]

def total_distance(tour):
    "The total distance between each pair of consecutive cities in the tour."
    return sum(distance(tour[i], tour[i-1]) for i in range(len(tour)))

City = complex

def distance(A, B):
    "The distance between two points."
    return abs(A - B)

A = City(300, 0)
B = City(0, 400)
distance(A, B)

500.0

def Cities(n):
    "Make a set of n cities, each with random coordinates."
    return set(City(random.randrange(18, 890), random.randrange(10, 500)) for c in range(n))

random.seed('seed')
cities8, cities10, cities100, cities1000 = Cities(8), Cities(10), Cities(100), Cities(1000)
cities8

tour = exact_TSP(cities8)

print(tour)
print(total_distance(tour))

((551+542j), (303+506j), (252+365j), (54+361j), (151+70j), (498+96j), (800+430j), (684+435j))
1990.388372313552

# Try All Non-Redundant Tours

def alltours(cities):
    "Return a list of tours, each a permutation of cities, but each one starting with the same city."
    start = first(cities)
    return [[start] + list(tour)
            for tour in itertools.permutations(cities - {start})]

def first(collection):
    "Start iterating over collection, and return the first element."
    for x in collection: return x

    alltours({1, 2, 3})

    [[1, 2, 3], [1, 3, 2]]

    alltours({1, 2, 3, 4})

    [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2]]

tour = exact_TSP(cities8)

print(tour)
print(total_distance(tour))

def plot_tour(algorithm, cities):
    "Apply a TSP algortihm to cities, and plot the resulting tour."
    t0 = time.time()
    tour = algorithm(cities)
    t1 = time.time()

    plotline(list(tour) + [tour[0]])
    plotline([tour[0]], 'rs')
    plt.show()
    print("{} city tour; total distance = {:.1f}; time = {:.3f} secs for {}".format(len(tour), total_distance(tour), t1-t0, algorithm.__name__))

def plotline(points, style='bo-'):
    "Plot a list of points (complex numbers) in the 2-D plane."
    X, Y = XY(points)
    plt.plot(X, Y, style)

def XY(points):
    "Given a list of points, return two lists: X coordinates, and Y coordinates."
    return [p.real for p in points], [p.imag for p in points]

plot_tour(exact_TSP, cities10)