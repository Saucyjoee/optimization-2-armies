from scipy.optimize import linprog
import numpy as np
import scipy

count = 0

strategy = []

for x in range(0, 8):
    for y in range(0, 8-x):
        strategy.append([x,y, 7-(x+y)])
        count += 1



print(count)
print(strategy)

def winner(num):
    return -1 if num < 0 else 0 if num == 0 else 1

payoff = np.array([[sum([winner(strategy[y][i] - strategy[x][i]) for i in range(3)]) for y in range(36)] for x in range(36)])

print(payoff)

# La modelling

# Coefficients for objective function: we want to maximize v, so we minimize -v
c = [0]*36 + [-1]

# Constraints, upper bound bro.
A_ub = []
b_ub = []

for j in range(36):
    constraint = [-payoff[i,j] for i in range(36)] + [1]
    A_ub.append(constraint)
    b_ub.append(0)

# Sum of probabilities = 1, matrix with equality constraints
A_eq = [[1]*36 + [0]]
b_eq = [1]

# Bounds: x_i ≥ 0, v free (can be negative)
bounds = [(0, 1)]*36 + [(None, None)]

#La solution, even has userexception that it throws if it doesn't work if you didn't download the library o_O

res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")

if res.success:
    optimal_strategy = res.x[:-1]
    game_value = res.x[-1]
    print("Optimal strategy for Antigonus:", optimal_strategy)
    print("Game value (expected payoff):", game_value)
else:
    print("LP failed:", res.message)