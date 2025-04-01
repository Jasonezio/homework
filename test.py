import requests
import time
import datetime

response = requests.get("https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=SRS&year=2025&rformat=json")

for date in response.json()["data"]:
    if datetime.datetime.today().strftime('%Y-%m-%d') == date[0]:
        print(date)