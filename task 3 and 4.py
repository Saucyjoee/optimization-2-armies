from scipy.optimize import linprog
import numpy as np
import scipy
import sys
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)

legions = 14

count = 0

strategy = []

for x in range(0, legions+1):
    for y in range(0, (legions+1)-x):
        strategy.append([x,y, legions-(x+y)])
        count += 1



print(count)
print(strategy)

def winner(num):
    return 1. if num < 0. else 0. if num == 0. else -1.

payoff = np.array([[sum([winner(strategy[y][i] - strategy[x][i]) for i in range(3)]) for y in range(count)] for x in range(count)])

plt.imshow(payoff)
plt.show()

def apply_strategy(M, Probs):
    #Probs is a list of size equal to the total strategy's
    for p in range(len(Probs)):
        M[p] *= Probs[p]
    return M


def find_strategy(Matrix, MIN_MAX = -1):
    # La modelling

    # Coefficients for objective function: we want to maximize v, so we minimize -v
    c = [0]*count + [MIN_MAX]

    # Constraints, upper bound bro.
    A_ub = []
    b_ub = []

    for j in range(count):
        constraint = [MIN_MAX*Matrix[i,j] for i in range(count)] + [MIN_MAX*-1]
        A_ub.append(constraint)
        b_ub.append(0)

    # Sum of probabilities = 1, matrix with equality constraints
    A_eq = [[1]*count + [0]]
    b_eq = [1]

    # Bounds: x_i ≥ 0, v free (can be negative)
    bounds = [(0, 1)]*count + [(None, None)]

    #La solution, even has userexception that it throws if it doesn't work if you didn't download the library o_O

    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")

    if res.success:
        optimal_strategy = res.x[:-1]
        game_value = res.x[-1]
        print("Optimal strategy for Antigonus:", optimal_strategy)
        print("Game value (expected payoff):", game_value)
        #print(sum(sum(apply_strategy(Matrix, optimal_strategy))) / count) # v
        #print(apply_strategy(Matrix, optimal_strategy))
    else:
        print("LP failed:", res.message)
    return optimal_strategy

find_strategy(payoff)

