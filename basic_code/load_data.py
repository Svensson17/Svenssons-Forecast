from basic_code.determine_data import determine_city, \
    determine_forecast_type, \
    verify_city, \
    determine_forecast_data
from basic_code.format_data import format_full_response, format_short_response
import prompt
from basic_code.const import forecast_api_key


def load_for_terminal():
    print("Welcome to the Svensson's Forecast!")
    while True:
        city = determine_city()
        forecast_type = determine_forecast_type(city)
        response = determine_forecast_data(city, forecast_api_key)
        if forecast_type == 'short':
             result = format_short_response(response)
             print(result['description'])
             print(result['temperature'])
        else:
            result = format_full_response(response)
            print(result['coordinates'])
            print(result['country'])
            print(result['temperature'])
            print(result['sky'])
            print(result['wind'])
        answer = prompt.string("Do you want to see another forecast?(yes/no) ")
        if answer == 'yes':
            continue
        else:
            print('Hasta La Vista!')
            break


def load_for_flask(fl_city, forecast_type):
    if not verify_city(fl_city):
        return {'city': 'No such city. Please, try again'}
    response = determine_forecast_data(fl_city, forecast_api_key)
    if forecast_type == 'short':
        return format_short_response(response)
    elif forecast_type == 'full':
        return format_full_response(response)
