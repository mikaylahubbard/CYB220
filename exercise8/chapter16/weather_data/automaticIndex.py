from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def getHighsAndLows(pathName):
    path = Path(pathName)
    lines = path.read_text(encoding='utf-8').splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)


    
    for index, column_header in enumerate(header_row):
        if column_header == "DATE":
            date_index = index
        if column_header == "TMAX":
            high_index = index
        if column_header == "TMIN":
            low_index = index
        if column_header == 'NAME':
            name_index = index

    dates, highs, lows = [], [], []
    for row in reader:
        if row[high_index] != '' and row[low_index] != '':
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[high_index])
            highs.append(high)
            low = int(row[low_index])
            lows.append(low)
            stationName = row[name_index]


    return {'dates': dates, 'highs': highs, 'lows': lows, 'name': stationName}


sitkaData = getHighsAndLows('sitka_weather_2021_full.csv')
deathData = getHighsAndLows('death_valley_2021_full.csv')

#plot the  temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(sitkaData['dates'], sitkaData['highs'], color='red')
ax.plot(sitkaData['dates'], sitkaData['lows'], color='blue')
ax.plot(deathData['dates'], deathData['highs'], color='orange')
ax.plot(deathData['dates'], deathData['lows'], color='green')

ax.set_title(f"High and Low temps: \n{sitkaData['name']} and {deathData['name']}", fontsize=16)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.legend(["Sitka Highs", "Sitka Lows", "Death Valley Highs", "Death Valley Lows"])
plt.show()
