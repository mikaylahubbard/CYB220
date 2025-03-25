from pathlib import Path
import json

import plotly.express as px


# Read data as a string and convert to a Python object.
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color':'Magnitude'},
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()

┌──(parallels㉿kali-gnu-linux-2023)-[~/exercise8/pcc_3e/chapter_16/mapping_global_datasets]
└─$ ls                                                                 
eq_data             fires.py            recent_eq_map.py
eq_explore_data.py  my_eq_world_map.py
eq_world_map.py     partial_programs

┌──(parallels㉿kali-gnu-linux-2023)-[~/exercise8/pcc_3e/chapter_16/mapping_global_datasets]
└─$ cat fires.py                                                       
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



┌──(parallels㉿kali-gnu-linux-2023)-[~/exercise8/pcc_3e/chapter_16/mapping_global_datasets]
└─$ ls                                                                 
eq_data             fires.py            recent_eq_map.py
eq_explore_data.py  my_eq_world_map.py
eq_world_map.py     partial_programs

┌──(parallels㉿kali-gnu-linux-2023)-[~/exercise8/pcc_3e/chapter_16/mapping_global_datasets]
└─$ cat my_eq_world_map.py                                             
from pathlib import Path
import json

import plotly.express as px

#read data as a string and convert to a python object
path = Path('eq_data/eq_data_1_day_m1.geojson')
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

fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='agsunset',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()

