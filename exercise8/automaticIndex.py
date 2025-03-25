from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

def getHighsAndLows(pathName):
    path = Path(pathName)
    lines = path.read_text(encoding='utf-8').splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    date_index = ''
    high_index = ''
    low_index = ''

    for index, column_header in enumerate(header_row):
        print(index, column)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-$d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_data)
        highs.append(high)
        lows.append(low)

        return [dates, highs, lows]


sitkaData = getHighsAndLows('sitka_weather_2021_full.csv')
deathData = getHighsAndLows('death_valley_2021_full.csv')
