import matplotlib.pyplot as plt
from numpy import random, std, pi, cos, sin
from graph import *


def rand_walker_1d(sample_size:int, num_steps:int):
    walkers = [0 for _ in range(sample_size)]           # List of walkers with location
    std_devs = []

    for _ in range(num_steps):                          # Changes position, num_steps times
        std_devs.append(std(walkers))
        for i in range(len(walkers)):
            walkers[i] += ((random.rand() * 2) - 1)     # Adds random number from -1 to 1
    return walkers, std_devs


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
    sample_size = 100000
    num_steps = 4

    walkers, std_devs = rand_walker_2d(sample_size, num_steps)
    # scatter_walker(walkers)
    pos_hist(walkers, num_steps, 100, 2, False)