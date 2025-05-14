from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/Fort_Wayne_data')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, preps = [], []
for row in reader:
    try:
        current_date =datetime.strptime(row[2], '%Y-%m-%d')
        prep = float(row[3])
    except ValueError:
        print(f'missing data for {current_date}')
    else:
        dates.append(current_date)
        preps.append(prep)

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, preps, color='red', alpha=0.5)

ax.set_title("Precepitation for 2020", fontsize=20)
ax.set_xlabel('', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation", fontsize=12)
ax.tick_params(labelsize=12)

plt.show()
