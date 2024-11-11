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
    body = json.loads(request.data)
    name = body.get("name")
    username = body.get("username")
    balance = body.get("balance", 0)
    user_id = DB.insert_user_table(name, username, balance)
    user = DB.get_user_by_id(user_id)
    if not user:
        return json.dumps({"error": "User not found"}), 400
    return json.dumps(user), 201
    

@app.route("/api/user/<int:user_id>/")
def get_user(user_id):
    user = DB.get_user_by_id(user_id)
    if not user:
        return json.dumps({"error": "User not found"}), 404
    return json.dumps(user), 200

@app.route("/api/user/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    user = DB.get_user_by_id(user_id)
    if not user:
        return json.dumps({"error": "User not found"})
    DB.delete_user_by_id(user_id)
    return json.dumps(user), 202

@app.route("/api/send/", methods=["POST"])
def send_money():
    body = json.loads(request)
    sender_id = body["sender_id"]
    if sender_id is None:
        return json.dumps({"error": "Sender not provided"}), 400
    receiver_id = body["receiver_id"]
    if receiver_id is None:
        return json.dumps({"error": "Receiver not provided"}), 400
    amount = body["amount"]
    if amount is None:
        return json.dumps({"error": "Amount not provided"}), 400
    
    sender = DB.get_user_by_id(sender_id)
    if not sender:
        return json.dumps({"error": "Sender not found"}), 404
    receiver = DB.get_user_by_id(receiver_id)
    if not receiver:
        return json.dumps({"error": "Receiver not found"}), 404

    initial_sender_balance = sender["balance"]
    if initial_sender_balance < amount:
        return json.dumps({"error": "Sender does not have enough funds"}), 400
    new_sender_balance = initial_sender_balance - amount

    initial_receiver_balance = receiver["balance"]
    new_receiver_balance = initial_receiver_balance + amount

    DB.update_user_balance_by_id(new_sender_balance, sender_id)
    receiver_info = DB.update_user_balance_by_id(new_receiver_balance, receiver_id)
    return 



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
