import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from datetime import timedelta

week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
df = pd.DataFrame(columns=["weekday","date","Description","Temperature °C"])

page = requests.get("https://forecast.weather.gov/MapClick.php?x=276&y=148&site=lox&zmx=&zmy=&map_x=276&map_y=148#.YVMW5ezivIU")
#print(page)

soup = BeautifulSoup(page.content, 'html.parser')

#this is for reading day value
div = soup.find_all('div',id="current_conditions_detail")[0]
td = div.find_all("td")

#date ="".join(today[-1].text.strip().split()[:2])
date ="".join(td[-1].text.strip().split()[:2])
date = date.replace("Sep","-9-")+"2021"
date = datetime.strptime(date,'%d-%m-%Y').date()

Temperature = td[-5].text.split()[-1].replace("(","").replace(")","")


weekday = week_days[date.weekday()]

df2 = pd.Series([weekday, date, None, Temperature], index=df.columns)
df = df.append(df2, ignore_index=True)

div = soup.find_all('div',class_="tombstone-container")
weekday = []

date_list = []
description = []
Temperature_initial = []
Temperature = []

for i in div:
    
    weekday.append(i.find("p", class_="period-name").text)
    date += timedelta(days=1)
    date_list.append(date)
    try:
        Temperature_initial.append(i.find("p", class_="temp temp-low").text)
    except:
        Temperature_initial.append(i.find("p", class_="temp temp-high").text)

for j in Temperature_initial:
    Temperature.append(str(int((int(j.split()[1])-32)/1.8))+"°C")

div_description = soup.find_all('div',class_="col-sm-10 forecast-text")
description = []
for el in div_description:
    description.append(el.text)

df2 = pd.DataFrame(list(zip(weekday, date_list, description, Temperature)), columns=df.columns)
df = df.append(df2, ignore_index=True)
print(df)