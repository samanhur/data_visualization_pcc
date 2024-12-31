from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

import os

# Changing project path to dataset file
os.chdir("../learning_sections/weather_data")


path = Path("sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


# # Checking column name and their position.
# for index, column_name in enumerate(header_row):
#    print(index, column_name)

# Extract dates and rainfall amount
# PRCP repersent daily rainfall amount.
dates, prcps = [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        prcp = float(row[5])
    except ValueError:
        print(f"Missing data : {current_date}")
    else:
        dates.append(current_date)
        prcps.append(prcp)
    
# Plot the high temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.bar(dates, prcps, color="blue")

# Format plot
ax.set_title("Daily Precipitation, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation Amount (in)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()