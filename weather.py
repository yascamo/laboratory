import requests
city = "Moscow,RU"
appid = "508ecf9b74675306871541c00f7e8ccf"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура:", data['main']['temp_max'])
print("Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("\nПрогноз погоды на неделю:")
for i in data['list']:
    print("Дата <",i['dt_txt'], "> \r\n Температура <",'{0:+3.0f}'.format(i['main']['temp']), "> \r\n Погодные условия <",
          i['weather'][0]['description'], "> \r\n Скорость ветра <", i['wind']['speed'], "> \r\n Видимость <", i['visibility'], ">")
    print("____________________________")