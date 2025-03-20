from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Cho phép frontend gọi API từ Flask

API_KEY = "e76a0f6f0fafee994449f97cc748c95a"  # API Key của bạn

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Invalid city name or API issue"}), 400

    data = response.json()
    return jsonify({
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Flask chạy trên port 5000
