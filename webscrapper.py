from bs4 import BeautifulSoup
import pandas as pd
import requests


#Web Scrapping
#codepen. io

#step 1 - beautifulsoup4 - this should be pep install
#step 2 - Requests
#step 3 - panda



page = requests.get('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XgRw_kczYVA')
soup = BeautifulSoup(page.content, 'html.parser')
week=soup.find (id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
#print(items[0].get_text())

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())



period_names = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

print(period_names)
print(short_desc)
print(temperatures)

weather_stuff = pd.DataFrame(
  {
    'period':period_names,
    'short_descriptions':short_desc,
    'temperatures':temperatures,
  })

print(weather_stuff)

weather_stuff.to_csv('weather.csv')
