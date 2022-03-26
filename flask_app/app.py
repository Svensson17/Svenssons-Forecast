from flask import Flask, render_template, request
from basic_code.download_inf import download_for_flask


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'What city do you want to check'


@app.route('/weather')
def forecast():
    fl_city = request.args['city']
    fl_forecast_type = request.args['type']
    return render_template('weather.html', item=download_for_flask(fl_city, fl_forecast_type))
#
#
# @app.route('/args')
# def args():
#     return render_template('args.html', title='Arguments', query=request.args.lists())
#
#
# @app.route('/json')
# def return_json():
#     response = dict(request.args.lists())
#
#     return jsonify(response)


if __name__ == '__main__':
    app.run()
