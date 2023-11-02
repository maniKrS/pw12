import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather/<city>')
def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=<your_api_key>'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
# i don't have open weather api
if __name__ == '__main__':
    app.run()
