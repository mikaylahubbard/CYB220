from pathlib import Path
import csv
import matplotlib.pyplot as plt

#a function to get the data
def getRainData(pathName, indexOfPrec):
    path = Path(pathName)
    lines = path.read_text(encoding='utf-8').splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    rainData = []
    for row in reader:
        rain = float(row[indexOfPrec])
        rainData.append(rain)
    return rainData

sitkaData = getRainData('sitka_weather_2021_full.csv', 5)
deathData = getRainData('death_valley_2021_full.csv', 3)

#plot
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(sitkaData, color="blue")
ax.plot(deathData, color="red")

#format
ax.set_title("Sitka vs. Death Valley Rainfall", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Amount of Rainfall (mm)', fontsize=16)
ax.tick_params(labelsize=16)
plt.legend(["Sitka", "Death Valley"])

plt.show()

