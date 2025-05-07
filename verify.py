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

payoff = np.matrix([[sum([winner(strategy[y][i] - strategy[x][i]) for i in range(3)]) for y in range(36)] for x in range(36)])

print(payoff)

def apply_strategy(M, Probs):
    #Probs is a list of size equal to the total strategy's
    for p in range(len(Probs)):
        M[p] *= Probs[p]
    return M

#print(apply_strategy(apply_strategy(payoff, [0 for i in range(36)]).transpose(), [1 for i in range(36)]))


