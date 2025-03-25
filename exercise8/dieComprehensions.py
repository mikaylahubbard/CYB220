from die import Die
import plotly.express as px

d8 = Die()

num_rolls = 1000
results = [d8.roll() for x in range(num_rolls + 1)]

possible = range(1, d8.num_sides + 1)
frequencies = [results.count(value) for value in possible]

title = f"Results of Rolling a D8 {num_rolls} times"
labels = {"x": "Result", "y":"frequency of result"}
fig = px.bar(x = possible, y = frequencies, title=title, labels=labels)
fig.show()

