from pathlib import Path
import csv

import plotly.express as px

#read in the file
path = Path('eq_data/world_fires_1_day.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

lats, lons, brightnesses, titles = [], [], [], []
for row in reader:
    lats.append(row[0])
    lons.append(row[1])
    brightnesses.append(float(row[2]))
    titleAsDate = row[5]
    titles.append(titleAsDate)

title = "World Fires"
print(brightnesses)

fig = px.scatter_geo(lat=lats, lon=lons,  
                     title=title,
                     color=brightnesses,
                     color_continuous_scale='agsunset',
                     labels={'color':'brightness'},
                     projection='natural earth',
                     hover_name=titles,
                    )
fig.show()

