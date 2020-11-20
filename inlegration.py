import matplotlib.pyplot as plt
from itertools import zip_longest

class polynomial:
    '''
    A class used to represent a polynomial

    ...

    Attributes
    ----------
    coeffs : list
        a list containing the polynomial coefficients.
        The ith item is the coefficient of x**i 
    '''

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __add__(self, other):
        '''adds coefficents in each polynomial'''
        return polynomial([sum(x) for x in zip_longest(self.coeffs, other.coeffs, fillvalue=0)])

    def __rmul__(self, factor:float):
        return polynomial([factor * x for x in self.coeffs])

    def __getitem__(self, i:int):
        return self.coeffs[i]

    def __setitem__(self, key:int, value):
        self.coeffs[key] = value
    
    def __str__(self):
        return(str(self.coeffs))
    
    def apply(self, x):
        output = 0
        for i in range(len(self.coeffs)):
            output += self.coeffs[i] * (x ** i)
        return output

    def integral(self):
        '''Returns polynomial integral of polynomial'''
        integr = polynomial([0])
        for i in range(len(self.coeffs)):
            integr.coeffs.append(self.coeffs[i] / (i + 1))
        return integr


def binom_expansion(n:int):
    """Binomial expansion in n^2 time"""
    coeffs = [0, 1, 0]
    for _ in range(n):
        # Creates next level of Pascal's triangle
        coeffs = [0] + [coeffs[i] + coeffs[i+ 1] for i in range(len(coeffs) - 1)] + [0] 
    return coeffs[1:-1]


def factorial(x:int):
    if x == 0:
        return 1
    n = 1
    for i in range(1, x + 1):
        n *= i
    return n


def double_integration(f1:polynomial, f2:polynomial, flip_pt:int):
    integr_f1 = f1.integral()
    integr_f2 = f2.integral()
    const = integr_f1.apply(flip_pt) - integr_f2.apply(flip_pt)

    for i in range(len(integr_f1.coeffs)):  # Recalculates integr_f1(A) to = integr_f1(A-1)
        coeff = integr_f1[i]
        integr_f1[i] = 0
        for k in range(i + 1):
            sign = (-1) ** (i - k) # f1 integral uses (A-1), so odd powers of (-1) are * -1
            integr_f1[k] += coeff * binom_expansions[i][k] * sign
    
    for i in range(len(integr_f2.coeffs)): # Recalculates integr_f1(A) to = integr_f1(A-1)
        coeff = integr_f2[i]
        integr_f2[i] = 0
        for k in range(i + 1):
            integr_f2[k] += coeff * binom_expansions[i][k]
    integr_sum = -1 * integr_f1 + integr_f2
    integr_sum[0] += const
    return integr_sum


def iterate_set(poly_set:list, n:int):
    '''Iterates the polynomials for the probability function of step n + 1

    Arguments
    -----
    poly_set : list
        list of polynomials
    n : int
        Number of steps
    '''
    poly_set = [polynomial([0])] + poly_set + [polynomial([0])] # f(x) = 0 borders on either side
    next_set = []
    for i in range(len(poly_set) - 1):
        next_set.append(double_integration(poly_set[i], poly_set[i + 1], 2 * i - n))
    return next_set


if __name__ == "__main__":
    n_max = 100

    binom_expansions = [binom_expansion(n) for n in range(n_max + 1)]
    poly_tree = [[polynomial([1])]]
    for n in range(1, n_max):
        poly_tree.append(iterate_set(poly_tree[-1], n))

    print("\n")
    # for i in range(len(poly_tree)):
    #     for item in poly_tree[i]:
    #         print(factorial(i) * item)
    #     print("\n")
    fac_i = factorial(n_max)
    coeffs_set = [fac_i * abs(x.coeffs[-3]) for x in poly_tree[-1]]
    print(coeffs_set)
    
    plt.plot(list(range(len(coeffs_set))), coeffs_set, "b-")
    plt.show()