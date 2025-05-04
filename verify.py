count = 0

strategy = []

for x in range(0, 8):
    for y in range(0, 8-x):
        strategy.append([x,y, 7-(x+y)])
        count += 1

print(count)
print(strategy)