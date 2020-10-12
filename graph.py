import matplotlib.pyplot as plt
from numpy import random, std, pi, cos, sin

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
    plt.title("Walker locations after " + str(num_steps) + " steps")
    plt.xlabel("Position")
    plt.ylabel("Frequency")
    plt.show()

def dist(x,y):
    return (x**2 + y**2)**0.5

def three_dim_rand_walker(sample_size:int, num_steps:int, limit:float):
    """Simulates a population of walkers moving up to 1 unit in a random direction
    Creates a histogram of the x positions of walkers who are at most 'limit' from 
    y=0 after num_steps steps
    """
    walkers = [[0,0] for _ in range(sample_size)] # List of walkers with location
    std_devs = []
    for _ in range(num_steps):
        # std_devs.append(std([walker[0] for walker in walkers]))
        for i in range(len(walkers)):
            radius = random.rand() # Movement magnitude, [0, 1]
            theta = random.rand() * 2 * pi # Movement angle, [0, two pi]
            walkers[i][0] += radius * cos(theta) # Adds movement to x
            walkers[i][1] += radius * sin(theta) # Adds movement to y
    x = [walker[0] for walker in walkers]
    y = [walker[1] for walker in walkers]
    plt.plot(x,y, "bo")
    plt.show()
    # plt.plot(std_devs)
    # plt.title("Standard Deviation by the Number of Steps")
    # plt.xlabel("Number of Steps")
    # plt.ylabel("Standard Deviation")
    # plt.text(4/6 * num_steps, 0.5, "n = " + str(sample_size))
    # plt.show()

    # walkers_on_x = []
    # for walker in walkers:
    #     if walker[1]**2 < limit ** 2:
    #         walkers_on_x.append(walker[0])

    walkers_on_x = [dist(walker[0],walker[1]) for walker in walkers]

    n, bins, patches = plt.hist(walkers_on_x, 100, density=1, facecolor='g', alpha=0.75)
    plt.title("Walker locations after " + str(num_steps) + " steps")
    plt.xlabel("Distance from Origin")
    plt.ylabel("Frequency")
    plt.show()

three_dim_rand_walker(100000, 2, 0.1)
