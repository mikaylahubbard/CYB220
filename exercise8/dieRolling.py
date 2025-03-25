from die import Die
import plotly.express as px

d8 = Die()

results = []
num_rolls = 1000
for roll_num in range(num_rolls + 1):
    result = d8.roll()
    results.append(result)

frequencies = []
possible = range(1, d8.num_sides+1)
for value in possible:
    frequency = results.count(value)
    frequencies.append(frequency)

title = f"Results of rolling a D8 {num_rolls} times"
labels = {'x':'Result', 'y': 'frequency of result'}
fig = px.bar(x=possible, y=frequencies, title=title, labels=labels)
fig.show()
