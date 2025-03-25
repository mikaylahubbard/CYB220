import matplotlib.pyplot as plt
from die import Die
from random_walk import RandomWalk

d8  = Die()

num_rolls = 500
results = [d8.roll() for x in range(num_rolls + 1)]

possible = range(1, d8.num_sides + 1)
frequencies = [results.count(value) for value in possible]



plt.style.use('classic')
plt.bar(possible, frequencies)
plt.title(f'Results of Rolling a D8 {num_rolls} times')
plt.xlabel("result")
plt.ylabel("frequency of result")
plt.show()

