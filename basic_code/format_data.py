def format_full_response(item):
    return {
        'coordinates': "The {}'s coordinates are {} lon, {} lat.".format(
            item['name'], item['coord']['lon'], item['coord']['lat']
        ),
        'country': 'The country is {}.'.format(item['sys']['country']),
        'temperature': 'The temperature is {0}, feels like {1} in Celsius.'.format(
            item['main']['temp'], item['main']['feels_like']
        ),
        'sky': 'The sky is in {0}, the pressure is {1}.'.format(
            item.get('weather')[0]['description'], item['main']['pressure']
        ),
        'wind': 'The wind speed is {0}, the direction is {1} degrees.'. format(
            item['wind']['speed'], item['wind']['deg']
        )
    }


def format_short_response(item):
    weather_item = item.get('weather')[0]
    temp_item = item.get('main')
    return {
        'temperature': 'The temperature is {} Celsius'.format(temp_item['temp']),
        'description': 'The sky is in {}'.format(weather_item['description']),
        'format_type': 'short'
    }
