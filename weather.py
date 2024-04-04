import requests
api_key = '117ae1c6b83eda16cd3027e038b986a6'
print("welcome to weather app")
city = input('Enter city name : ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    cel=int(temp-273.15)
    desc = data['weather'][0]['description']
    print(f'Temperature of the {city} is : {cel} celsius')
    print(f'{city} has {desc}')
else:
    print('Error fetching weather data')
