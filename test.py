from flask import Flask, request, jsonify
import mysql.connector as mc
from mysql.connector import Error
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

SECRET_KEY = 'Honey123'  # Keep this secret and secure

def db_cn():
    return mc.connect(
        host="localhost",
        user="root",
        password="Honey123@#",
        database="website"
    )

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # Extract token from "Bearer <token>"

        if not token:
            return jsonify({"Error": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"Error": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"Error": "Invalid token!"}), 401

        return f(data, *args, **kwargs)

    return decorated

@app.route('/login', methods=['POST'])
def Log():
    try:
        db = db_cn()
        if not db.is_connected():
            return jsonify({"Error": "Database connection failed"}), 500

        cursor = db.cursor()
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"Error": "All Fields are Required..."}), 400

        query = """SELECT * FROM members WHERE username = %s AND password = %s"""
        cursor.execute(query, (username, password))
        result = cursor.fetchall()
        db.commit()

        if result:
            payload = {
                'username': username,
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5)  # Token expiration
            }
            encoded_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

            return jsonify({
                'message': 'Login successful',
                'token': encoded_token
            })

        return jsonify({"Error": "Username and password mismatch..."}), 401

    except Error as er:
        return jsonify({"Error": f"Unable to connect to the server: {str(er)}"}), 500
    finally:
        if db.is_connected():
            cursor.close()
            db.close()

@app.route('/verify-token', methods=['GET'])
@token_required
def verify_token(data):
    return jsonify({"message": "Token is valid", "user": data}), 200

if __name__ == '__main__':
    app.run(debug=True)
