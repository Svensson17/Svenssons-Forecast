def format_full_response(item):
    print(
        "The {}'s coordinates are {} lon, {} lat.".format(
            item['name'], item['coord']['lon'],
            item['coord']['lat']
        )
    )
    print('The country is {}.'.format(item['sys']['country']))
    print(
        'The temperature is {0}, feels like {1} in Celsius.'.format(
            item['main']['temp'],
            item['main']['feels_like']
        )
    )
    print(
        'The sky is in {0}, the pressure is {1}.'.format(
            item.get('weather')[0]['description'],
            item['main']['pressure']
        )
    )
    print(
        'The wind speed is {0}, the direction is {1} degrees.'. format(
            item['wind']['speed'],
            item['wind']['deg']
        )  # data for terminal
    )
    return "The {0}'s coordinates are {1} lon, {2} lat.\
    The country is {3}.The temperature is {4}, feels like {5} in Celsius.\
    The sky is in {6}, the pressure is {7}.\
    The wind speed is {8}, the direction is {9} degrees.".format(
        item['name'],
        item['coord']['lon'],
        item['coord']['lat'],
        item['sys']['country'],
        item['main']['temp'],
        item['main']['feels_like'],
        item.get('weather')[0]['description'],
        item['main']['pressure'],
        item['wind']['speed'],
        item['wind']['deg']
    )  # data for flask


def format_short_response(item):
    weather_item = item.get('weather')[0]
    temp_item = item.get('main')
    print('The sky is in {}'.format(weather_item['description']))
    print('The temperature is {} Celsius'.format(temp_item['temp']))
    # data for terminal
    return 'The sky is in {}.The temperature is {} Celsius'.format(
        weather_item['description'],
        temp_item['temp']
    )  # data for flask
