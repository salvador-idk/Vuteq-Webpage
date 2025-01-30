from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder = 'frontend/build', static_url_path='')

#Enable CORS for all routes
CORS(app)

@app.route('/api/data', methods = ['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask! It works!!!"})

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # Serve any static files from the React build directory
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port = 5000)
    