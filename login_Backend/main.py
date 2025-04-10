from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from Register import Reg
from Login import Log, ur_name, passwd
import jwt
from functools import wraps

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})


SECRET_KEY = 'Honey123'  # Keep this secret and secure


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


# For Registration
@app.route("/Register", methods=["POST"])
def Regi():
    data = request.get_json()
    return Reg(data)


# For Login
@app.route("/Login", methods=["POST", "OPTIONS"])
def Login():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        return response, 200  # Important: Return 200 OK
    else:
        data = request.get_json()
        return Log(data)


# For Updating Password
@app.route("/Login/password", methods=["POST"])
def password():
    data = request.get_json()
    return passwd(data)


# For Updating Username
@app.route("/Login/username", methods=["POST"])
def user_name():
    data = request.get_json()
    return ur_name(data)


# New API to Verify Token
@app.route("/verify-token", methods=["GET"])
@token_required
def verify_token(data):
    return jsonify({"message": "Token is valid", "user": data}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
