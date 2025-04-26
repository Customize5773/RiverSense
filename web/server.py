# server.py
# Local Webserver for RiverSense Monitoring
# Author: [Rasya Pratama]
# Date: [27 Apr 2025]

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Global variable to store latest sensor status
current_water_level = "UNKNOWN"

ESP32CAM_STREAM_URL = "http://192.168.1.50/"  # Change to your ESP32-CAM IP

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>RiverSense Monitoring</title>
</head>
<body>
    <h1>RiverSense - Real-Time Monitoring</h1>
    <h2>Water Level Status: {{ water_level }}</h2>
    <h3>Camera Stream:</h3>
    <img src="{{ cam_url }}" width="640" height="480" alt="ESP32-CAM Stream">
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, water_level=current_water_level, cam_url=ESP32CAM_STREAM_URL)

@app.route('/update_level', methods=['POST'])
def update_level():
    global current_water_level
    data = request.get_json()
    if 'level' in data:
        current_water_level = data['level']
        return jsonify({"status": "success", "message": "Water level updated"}), 200
    else:
        return jsonify({"status": "error", "message": "Missing 'level' field"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
