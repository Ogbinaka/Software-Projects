import requests

url = "https://flood-api.open-meteo.com/v1/flood?latitude=7.38&longitude=3.91&daily=river_discharge,river_discharge_mean,river_discharge_median,river_discharge_max,river_discharge_min,river_discharge_p25,river_discharge_p75&start_date=1984-01-01&end_date=2023-12-31&forecast_days=183"

response = requests.get(url)

if response.status_code == 200:
   data = response.json()
   print(response.json())
else:
   print("Error occurred while fetching data. Status code:", response.status_code)


#import pandas as pd

#importing pandas and renaming it as pd because it is great tool for reading csv files in a python environment

#df = pd.read_csv("flood_data.csv")

#execute
#df

#df.tail(9)