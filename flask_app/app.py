from flask import Flask, render_template, request
from basic_code.load_data import load_for_flask


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'What city do you want to check'


@app.route('/weather')
def forecast():
    fl_city = request.args['city']
    fl_forecast_type = request.args['type']
    return render_template('weather.html', item=load_for_flask(fl_city, fl_forecast_type))


if __name__ == '__main__':
    app.run()
