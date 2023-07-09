import json
import random
import time
from datetime import datetime
import requests
from flask import Flask, Response, render_template
application = Flask(__name__)
random.seed()


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/chart-data')
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': 'Material Particulado', 'value': random.randint(5, 20)})
            yield f"data:{json_data}\n\n"
            time.sleep(3)

    return Response(generate_random_data(), mimetype='text/event-stream')


@application.route('/chart-data2')
def chart_data2():
    def generate_random_data2():
        while True:
            json_data = json.dumps(
                {'time2': 'Material Particulado', 'value2': random.randint(5, 20)})
            yield f"data:{json_data}\n\n"
            time.sleep(3)

    return Response(generate_random_data2(), mimetype='text/event-stream')


@application.route('/chart-data3')
def chart_data3():
    def generate_random_data3():
        while True:
            json_data = json.dumps(
                {'time3': 'Material Particulado', 'value3': random.randint(5, 20)})
            yield f"data:{json_data}\n\n"
            time.sleep(3)

    return Response(generate_random_data3(), mimetype='text/event-stream')


@application.route('/chart-data4')
def chart_data4():
    def generate_random_data4():
        while True:
            json_data = json.dumps(
                {'time4': 'Temperatura', 'value4': random.randint(-10, 10)})
            yield f"data:{json_data}\n\n"
            time.sleep(3)

    return Response(generate_random_data4(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
