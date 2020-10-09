import matplotlib.pyplot as plt
from numpy import random, std

def two_dim_rand_walker(sample_size:int, num_steps:int):
    walkers = [0 for _ in range(sample_size)] # List of walkers with location
    std_devs = []
    for _ in range(num_steps):
        std_devs.append(std(walkers))
        for i in range(len(walkers)):
            walkers[i] += ((random.rand() * 2) - 1) # Adds random number from -1 to 1
    plt.plot(std_devs)
    plt.title("Standard Deviation by the Number of Steps")
    plt.xlabel("Number of Steps")
    plt.ylabel("Standard Deviation")
    plt.text(4/6 * num_steps, 0.5, "n = " + str(sample_size))
    plt.show()

    n, bins, patches = plt.hist(walkers, 100, density=1, facecolor='g', alpha=0.75)
    plt.show()

two_dim_rand_walker(1000000, 100)
