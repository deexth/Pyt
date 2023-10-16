import csv
import plotly.express as px
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from plotly import offline


path = Path("data/fires 2021/modis_2021_United_States.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

brights, lats, lons = [], [], []
brightness_row = header_row.index('brightness')
lat_row = header_row.index('latitude')
lon_row = header_row.index('longitude')

for row in reader:
    try:
        brights.append(float(row[brightness_row]))
        lats.append(float(row[lat_row]))
        lons.append(float(row[lon_row]))
    except ValueError:
        print(f"Data missing.")
        continue

title = "Global wildfire activity"
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
        color=brights,
        color_continuous_scale='Viridis',
        labels={'color':'Brightness'},
        projection='natural earth',
    )

# plot the data
# fig.show()
offline.plot(fig, filename='global_wildfire_activity.html')