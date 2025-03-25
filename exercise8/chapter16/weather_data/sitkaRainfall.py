from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#for index, col in enumerate(header_row):
 #   print(index, col)


#storing the precipitation data in a list
rainData = []
for row in reader:
    rain = float(row[5])
    rainData.append(rain)

#plot the precipitation
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(rainData, color='blue')

#format the plot
ax.set_title("Sitka Rainfall", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Amount of Rainfall (mm)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

