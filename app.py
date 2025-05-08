<<<<<<< HEAD
#app.py
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector

app = Flask(__name__, static_folder = 'frontend/build', static_url_path='')

#Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "*"}}) #Allow all origins for /api routes

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',  # 127.0.0.1 Your MySQL host
        user='root',  # Your MySQL username
        password='admin',  # Your MySQL password
        database='webpage',  # Your MySQL database name
        port = '3308',
        auth_plugin='mysql_native_password'
    )
    return connection

@app.route('/api/employees', methods=['GET'])
def get_employees():
    connection = None
    cursor = None
    try:
        
        connection = get_db_connection()
        cursor = connection.cursor(dictionary = True)
        cursor.execute('SELECT * FROM employees')
        employees = cursor.fetchall()
        return jsonify(employees)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

@app.route('/api/data_flask', methods = ['GET'])
def get_data_flask():
    return jsonify({"message": "Hello from Flask! It works!!!"})

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    # Serve any static files from the React build directory
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True, host='10.1.44.116', port = 5001)
=======
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
>>>>>>> 002be84fd66267940b29a06c94baff2b3e85224d
    