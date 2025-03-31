from flask import Flask, request, jsonify
from flask_jwt_extended import decode_token, JWTManager
import os

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY", "secret")
jwt = JWTManager(app)

@app.route("/auth", methods=["POST"])
def verify_token():
    data = request.json
    token = data.get("token")

    if not token:
        return jsonify({"login": False, "data": "error"}), 400

    try:
        decoded = decode_token(token)
        return jsonify({"login": True, "data": decoded})
    except Exception:
        return jsonify({"login": False, "data": "error"}), 401

if __name__ == "__main__":
    app.run(debug=True)
