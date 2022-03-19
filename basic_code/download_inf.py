import requests
from basic_code.determine_data import determine_city, determine_forecast_type
from basic_code.formatter import format_full_response, format_short_response
import prompt
from basic_code.const import forecast_api_key


def download():
    print("Welcome to the Svensson's Forecast!")
    while True:
        city = determine_city()
        forecast_type = determine_forecast_type(city)
        response_api = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric".format(
                city, forecast_api_key
            )
        )
        current_inf = response_api.json()
        if forecast_type == 'short':
            format_short_response(current_inf)
        else:
            format_full_response(current_inf)
        answer = prompt.string("Do you want to see another forecast?(yes/no) ")
        if answer == 'yes':
            continue
        else:
            print('Hasta La Vista!')
            break
