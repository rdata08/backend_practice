from datetime import datetime
import json

import db
from flask import Flask, request

app = Flask(__name__)

DB = db.DatabaseDriver()

@app.route("/api/users/")
def get_all_users():
    return json.dumps({"users": DB.get_all_users()}), 200


@app.route("/api/users/", methods=["POST"])
def create_user():
    pass

@app.route("/api/user/<int:user_id>/")
def get_user(user_id):
    pass

@app.route("/api/user/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    pass

@app.route("/api/send/", methods=["POST"])
def send_money():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
