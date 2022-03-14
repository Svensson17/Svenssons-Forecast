import prompt
import requests


def determine_city():
    city = prompt.string("What city do you want to check? ")
    return city


def determine_forecast_type(city):
    forecast_type = prompt.string(
        "What type of forecast do you want to see in {0}? (short/full): ".format(city)
    )
    print("The {0} forecast in {1} :".format(forecast_type, city))
    return forecast_type


def verify_city(city):
    url = "https://api.apilayer.com/geo/city/name/{}".format(city)
    payload = {}
    headers = {
        "apikey": "ycvkBrGzaM6Dwzq5hXGbBzh6BCsj9G6s"
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    return status_code
