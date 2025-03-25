from die import Die
import plotly.express as px

d1 = Die(6)
d2 = Die(6)
d3 = Die(6)

results = []
num_rolls = 1000
for roll_num in range(num_rolls + 1):
    result = d1.roll() + d2.roll() + d3.roll()
    results.append(result)

frequencies = []
possible = range(3, 6*3)
for value in possible:
    frequency = results.count(value)
    frequencies.append(frequency)

title = f"Results of rolling 3 D6 Dies {num_rolls} times"
labels = {"x":"Result", "y": "Frequency of Result"}
fig = px.bar(x=possible, y=frequencies, title=title, labels=labels)
fig.show()
