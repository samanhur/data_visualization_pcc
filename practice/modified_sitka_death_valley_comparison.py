import csv
from datetime import datetime
from pathlib import Path


import matplotlib.pyplot as plt

import os


def get_weather_data(path):
    """
    Get the highs and lows from a data file,
    and return a tuple of dates, highs and lows values.
    :return: dates, highs, lows.
    """
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    row_indexes = []
    for index, column_title in enumerate(header_row):
        if column_title in ["DATE", "TMAX", "TMIN"]:
            row_indexes.append(index)

    dates, highs, lows = list(), list(), list()

    # Extract dates, high  and low temperatures.
    for row in reader:
        current_date = datetime.strptime(row[row_indexes[0]], "%Y-%m-%d")
        try:
            high = int(row[row_indexes[1]])
            low = int(row[row_indexes[2]])

        except ValueError:
            print(f"Missing data for {current_date}")

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


# Changing project path to dataset file
os.chdir("../learning_sections/weather_data")


# Get weather data for sitka
path = Path("sitka_weather_2021_simple.csv")
sitka_dates, sitka_highs, sitka_lows = get_weather_data(path)

# Get weather data for death valley.
path = Path("death_valley_2021_simple.csv")
dv_dates, dv_highs, dv_lows = get_weather_data(path)


# Plot weather data.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()

# for sitka
ax.plot(sitka_dates, sitka_highs, color="red", alpha=0.6)
ax.plot(sitka_dates, sitka_lows, color="blue", alpha=0.6)
ax.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor="blue", alpha=0.15)

# for death valley
ax.plot(dv_dates, dv_highs, color="red", alpha=0.3)
ax.plot(dv_dates, dv_lows, color="blue", alpha=0.3)
ax.fill_between(dv_dates, dv_highs, dv_lows, facecolor="blue", alpha=0.05)

# Format plot.
title = "Daily high and low temperatures - 2021"
title += "\nSitka, AK and Death Valley, CA"
ax.set_title(title, fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.set_ylim(0, 150)

plt.show()
