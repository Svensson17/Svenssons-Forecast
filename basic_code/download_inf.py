import requests
from basic_code.determine_data import determine_city, determine_forecast_type


def download():
    city = determine_city()
    type = determine_forecast_type(city)
    api_key = '609bbe56a6793ee128b3e9e72e9b4f97'
    response_api = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}".format(city, api_key)
    )
    current_inf = response_api.json()
    if type == 'short':
        weather_current_inf = current_inf.get('weather')[0]
        temp_current_inf = current_inf.get('main')
        print('The weather is {}'.format(weather_current_inf['main']))
        print('The temperature is {} Fahrenheit'.format(temp_current_inf['temp']))
    elif type == 'full':
        for key, value in current_inf.items():
            print(key, ':', value)
    else:
        print('The wrong input')
