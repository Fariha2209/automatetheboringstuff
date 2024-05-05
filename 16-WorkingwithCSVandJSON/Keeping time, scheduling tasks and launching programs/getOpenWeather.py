import json, requests, sys

APPID = '7f842732dd9598f972efd45b98b51e4e'

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city-name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

url ='https://api.openweathermap.org/data/2.5/weather?lat=33.44&lon=-94.04&appid=%s' % (APPID)
print(url)
#url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s' % (location, APPID)
#print(url)
response = requests.get(url)
response.raise_for_status()

print(response.text)

weatherData = response.json()

print('Current weather in %s:' % (location))
print(weatherData['weather'][0]['main'], '-', weatherData['weather'][0]['description'])
print('IT WORKED!')
