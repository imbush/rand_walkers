import matplotlib.pyplot as plt
from numpy import random, std, pi, cos, sin, polyfit
from graph import *


def rand_walker_1d(sample_size:int, num_steps:int):
    walkers = [0 for _ in range(sample_size)]           # List of walkers with location
    std_devs = []
    means = []

    for _ in range(num_steps):                          # Changes position, num_steps times
        std_devs.append(std(walkers))
        means.append(sum(walkers)/len(walkers))
        for i in range(len(walkers)):
            walkers[i] += ((random.rand() * 3) - 1)     # Adds random number from -1 to 1
    return walkers, std_devs, means


def rand_walker_2d(sample_size:int, num_steps:int):
    """Simulates a population of walkers that move up
    to 1 unit in a random direction num_steps times
    """
    walkers = [[0,0] for _ in range(sample_size)]       # List of walkers with location
    std_devs = []
    for _ in range(num_steps):
        std_devs.append(std([dist(walker[0],walker[1]) for walker in walkers]))
        for i in range(len(walkers)):
            radius = random.rand()                      # Movement magnitude, [0, 1]
            theta = random.rand() * 2 * pi              # Movement angle, [0, two pi]
            walkers[i][0] += radius * cos(theta)        # Adds movement to x
            walkers[i][1] += radius * sin(theta)        # Adds movement to y
    return walkers, std_devs


if __name__ == "__main__":
    sample_size = 1000000
    num_steps = 100

    walkers, std_devs, means = rand_walker_1d(sample_size, num_steps)
    # scatter_walker(walkers)
    # print(std_devs)
    # std_by_steps(std_devs, num_steps, sample_size)
    # pos_hist(walkers=walkers, num_steps=num_steps, num_bins=100, dimensions=1, by_radius=True, density=1)
    mean_by_steps(means, num_steps, sample_size)