import plotly.express as px
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()


df = px.data.iris()
point_numbers = range(rw.num_points)
title = "Random Walk"
labels = {"x": "X direction", "index":"Y direction", "color": "Timing of Walk"}
fig = px.scatter(x=rw.x_values, y=rw.y_values, color=point_numbers, title=title, labels=labels)
fig.show()
