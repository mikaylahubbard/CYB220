from pathlib import Path
import json

import plotly.express as px

#read data as a string and convert to a python object
path = Path('eq_data/recent_data.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#examine - extract magnitudes and location data
all_eq_dicts = all_eq_data['features']


mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

title = all_eq_data['metadata']['title']
absolute_mags = [abs(mag) for mag in mags]

fig = px.scatter_geo(lat=lats, lon=lons, 
                     size=absolute_mags, 
                     title=title,
                    color=absolute_mags,
                     color_continuous_scale='agsunset',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                    )
fig.show()
