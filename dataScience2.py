import plotly.express as px
import pandas as pd
import csv

rows = []

with open("Stars.csv", 'r') as f:
    csvreader = csv.reader(f)

    for row in csvreader:
        rows.append(row)

headers = rows[0]

star_data = rows[1:]

star_masses = []

star_radiuses = []

star_gravities = []

for star in star_data:
    if star[3] == '?' or star[4] == '?' or star[5] == '?':
        star_data.remove(star)
    else:
        star_masses.append(float(star[3]))
        star_radiuses.append(float(star[4]))
        star_gravities.append(float(star[5]))

fig = px.scatter(x = star_masses, y = star_radiuses, size = star_gravities, range_y = (-2e+8, 3e+9), range_x = (-1e+31, 2.1e+32), labels = dict(x = 'Mass of Star', y = 'Radius of Star'))

fig.show()
