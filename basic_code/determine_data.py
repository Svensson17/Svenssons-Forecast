import prompt
import requests
from basic_code.const import verify_city_api_key


def determine_city():
    while True:
        city = prompt.string("What city do you want to check? ")
        if verify_city(city):
            return city
        print('Please,type the right city')


def determine_forecast_type(city):
    forecast_type = prompt.string(
        "What type of forecast do you want to see in {0}? (short/full): ".format(city)
    )
    print("The {0} forecast in {1} :".format(forecast_type, city))
    return forecast_type


def verify_city(city):
    url = "https://api.apilayer.com/geo/city/name/{}".format(city)
    headers = {"apikey": verify_city_api_key}
    response = requests.get(url, headers=headers)
    return True if response.status_code == 200 else False


def determine_forecast_data(city, api_key):
    response_api = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric".format(
            city, api_key
        )
    )
    current_inf = response_api.json()
    return current_inf
