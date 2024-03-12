from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/error')
def get_error():
    return jsonify({'Error': '500 Internal Server Error'}), 500


@app.route('/success')
def get_success():
    return 'Successful'


@app.route('/')
def index():
    return """
    <h1>
        Flask
    </h1>
    <ul>
        <li><a href='/error'>This link is for error</a></li>
        <li><a href='/success'>This link is for success</a></li>
    </ul>

    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)