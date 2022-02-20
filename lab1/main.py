# Code cell 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium

# code cell 2
# This should be a local path
dataset_path = './data/Map-Crime_Incidents-Previous_Three_Months.csv'
# read the original dataset (in comma separated values format) into a DataFrame
SF = pd.read_csv(dataset_path)

# code cell 3
#!head -n 5 ./Data/Map-Crime_Incidents-Previous_Three_Months.csv

# Code cell 4
pd.set_option('display.max_rows', 100) #Visualize 10 rows
print(SF)

# Code cell 5
print(SF.columns)

# Code cell 6
print(len(SF))

# Code cell 7
SF['Month'] = SF['Date'].apply(lambda row: int(row[0:2]))
SF['Day'] = SF['Date'].apply(lambda row: int(row[3:5]))

# Code cell 8
print(SF['Month'][0:2])
print(SF['Day'][0:2])

# Code cell 9
print(type(SF['Month'][0]))

# Code cell 10
del SF['IncidntNum']

# Code cell 11
SF.drop('Location', axis=1, inplace=True)

# Code cell 12
print(SF.columns)

# Code cell 13
CountCategory = SF['Category'].value_counts()
print(CountCategory)

# Code cell 14
SF['Category'].value_counts(ascending=True)

# Code cell 15
print(SF['Category'].value_counts(ascending=True))

# code cell 16
# Possible code for the challenge question
print(SF['PdDistrict'].value_counts(ascending=True))

# Code cell 17
AugustCrimes = SF[SF['Month'] == 8]
print(AugustCrimes)

# code cell 18
AugustCrimes = SF[SF['Month'] == 8]
AugustCrimesB = SF.query('Month == 8 and Category == "BURGLARY"')
print(len(AugustCrimes), len(AugustCrimesB))

# Code cell 19
Crime0704 = SF.query('Month == 7 and Day == 4')
print(Crime0704)

# Code cell 20
print(SF.columns)

# Code cell 21
plt.plot(SF['X'],SF['Y'], 'ro')
plt.show()

# Code cell 22
pd_districts = np.unique(SF['PdDistrict'])
pd_districts_levels = dict(zip(pd_districts, range(len(pd_districts))))
print(pd_districts_levels)

# Code cell 23
SF['PdDistrictCode'] = SF['PdDistrict'].apply(lambda row: pd_districts_levels[row])

# Code cell 24
plt.scatter(SF['X'], SF['Y'], c=SF['PdDistrictCode'])
plt.show()

# Code cell 25
from matplotlib import colors
districts = np.unique(SF['PdDistrict'])
print(list(colors.cnames.values())[0:len(districts)])

# Code cell 26
color_dict = dict(zip(districts, list(colors.cnames.values())[0:-1:len(districts)]))
print(color_dict)

# Code cell 27
map_osm = folium.Map(location=[SF['Y'].mean(), SF['X'].mean()], zoom_start = 12)
plotEvery = 50
obs = list(zip( SF['Y'], SF['X'], SF['PdDistrict']))
for el in obs[0:-1:plotEvery]:
    folium.CircleMarker(el[0:2], color=color_dict[el[2]], fill_color=el[2],radius=10).add_to(map_osm)

# Code cell 28
map_osm.save("./data/map.html")