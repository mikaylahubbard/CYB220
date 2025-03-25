from die import Die
import plotly.express as px

d1 = Die()
d2 = Die()

results = []
num_rolls = 500
for roll_num in range(num_rolls + 1):
   result = d1.roll() * d2.roll()
   results.append(result)

frequencies = []
possible = range(1, d1.num_sides * d2.num_sides)
for value in possible:
    frequency = results.count(value)
    frequencies.append(frequency)

title = f"Multiplication of the results of  rolling 2 D8s {num_rolls} times"
labels = {"x":"Result", "y": "Frequency of Result"}
fig = px.bar(x = possible, y = frequencies, title=title, labels=labels)
fig.show()
