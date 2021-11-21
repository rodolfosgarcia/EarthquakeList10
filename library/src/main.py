import requests
from geopy import distance
import numpy as np
import pandas as pd


url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'

response = requests.get(url)

lat = input("Enter Latitude: ")
lon = input("Enter Longitude: ")
manualInput = (lat, lon)
#manualInput = (19.2203333333333, -155.442666666667)

out = []

for eq in response.json()['features']:
    EqTitle = eq['properties']['title']
    latLonEq = (eq['geometry']['coordinates'][1], eq['geometry']['coordinates'][0])
    distFromCityKM = distance.distance(manualInput, latLonEq).km

    out.append([EqTitle, float(distFromCityKM), latLonEq])

df = pd.DataFrame(out)
dfSorted = df.sort_values(by=(1), ascending=True) #Sorting by Distance from City in question
df = df.head(20).drop_duplicates([1]) #removing duplicated LAT LONG for the first 20 ocurrences after sorting (better performance)
dfSorted.columns = ['Earthquake Name', 'Distance in KM', 'Location Lat/Long'] #inserting header

print(dfSorted.head(10).to_string(index=False))