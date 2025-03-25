from pathlib import Path
import csv
import matplotlib.pyplot as plt

#function to get the data
def getRainData(pathName, indexOfPrec):
    path = Path(pathName)
    lines = path.read_text(encoding='utf-8').splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    rainData = []
    count = 0
    for row in reader:
        if count >=365:
            exit
        else:
            rain = float(row[indexOfPrec])
            rainData.append(rain)
            count = count + 1
    return rainData

sitkaData = getRainData('sitka_weather_2021_full.csv', 5)
deathData = getRainData('death_valley_2021_full.csv', 3)
sanFranData = getRainData('24CityWeatherCsvFiles/weather-us/sanfrancisco.csv',  20)



#plot
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(sitkaData, color="blue")
ax.plot(deathData, color="red")
ax.plot(sanFranData, color="yellow")

#format
ax.set_title("Sitka vs. Death Valley vs. San Francisco Rainfall")
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Amount of Rainfall', fontsize=16)
ax.tick_params(labelsize=16)
plt.legend(['Sitka', 'Death Valley', 'San Francisco'])

plt.show()
