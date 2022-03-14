

def format_full_response(item):
    if isinstance(item, dict):
        for key, value in item.items():
            if isinstance(value, dict):
                format_full_response(value)
            else:
                print(key, '->', value)


def format_short_response(item):
    weather_item = item.get('weather')[0]
    temp_item = item.get('main')
    print('The weather -> {}'.format(weather_item['main']))
    print('The temperature -> {} Celsius'.format(temp_item['temp']))
