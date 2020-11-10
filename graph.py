import matplotlib.pyplot as plt
from numpy import random, std, pi, cos, sin

def pos_hist(walkers:list, num_steps:int, num_bins:int, dimensions:int, by_radius = True):
    if dimensions == 1:
        n, bins, patches = plt.hist(walkers, num_bins, density=1, facecolor='g', alpha=0.75)
        plt.title("Walker locations after " + str(num_steps) + " steps")
        plt.xlabel("Position")
        plt.ylabel("Frequency")
        plt.show()
    elif dimensions == 2:
        if by_radius:
            walkers_dist = [dist(walker[0],walker[1]) for walker in walkers]

            n, bins, patches = plt.hist(walkers_dist, num_bins, density=1, facecolor='g', alpha=0.75)
            plt.title("Walker locations after " + str(num_steps) + " steps")
            plt.xlabel("Distance from Origin")
            plt.ylabel("Frequency")
            plt.show()
        else: # Scales the bin size by the inverse of the circumference of the circle with the radius in the middle of the bin
            walkers_dist = [dist(walker[0],walker[1]) for walker in walkers]
            n, bins, patches = plt.hist(walkers_dist, num_bins, density=0)
            for i in range(len(n)):
                bins[i] = (bins[i] + bins[i + 1]) / 2
                n[i] = n[i] / (pi * (bins[i]) ** 2)
            plt.plot(bins[:-1], n, "b.")
            plt.show()


def dist(x:float, y:float) -> float:
    return (x ** 2 + y ** 2) ** 0.5


def std_by_steps(std_devs:list, num_steps:int, sample_size:int):
    plt.plot(std_devs)
    plt.title("Standard Deviation by the Number of Steps")
    plt.xlabel("Number of Steps")
    plt.ylabel("Standard Deviation")
    plt.text(4/6 * num_steps, 0.5, "n = " + str(sample_size))
    plt.show()


def scatter_walker(walkers):
    x = [walker[0] for walker in walkers]
    y = [walker[1] for walker in walkers]
    plt.plot(x, y, "b.")
    plt.show()