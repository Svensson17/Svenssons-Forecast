import prompt


def determine_city():
    print("Welcome to the Svenssons Forecast!")
    city = prompt.string("What city do you want to check? ")
    return city


def determine_forecast_type(city):
    forecast_type = prompt.string("What type of forecast do you want to see in {0}? (short/full): ".format(city))
    print("The {0} forecast in {1} :".format(forecast_type, city))
    return forecast_type
