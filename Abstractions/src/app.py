from db import db
from flask import Flask
import json

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route("/api/courses/")
def get_courses():
    pass

@app.route("/api/course/", methods=["POST"])
def create_course():
    pass

@app.route("/api/courses/<int:course_id>/")
def get_course():
    pass

@app.route("/api/courses/<int:course_id>/", methods=["DELETE"])
def delete_course():
    pass

@app.route("/api/users/", methods=["POST"])
def create_user():
    pass

@app.route("/api/users/<int:user_id>/")
def get_user():
    pass

@app.route("/api/courses/<int:course_id>/add/", methods=["POST"])
def add_user_to_course():
    pass

@app.route("/api/courses/<int:course_id>/assignment/", methods=["POST"])
def create_assignment():
    pass

def success_response(data, code = 200):
    return json.dumps(data), code

def failure_response(message, code = 400):
    return json.dumps({"error": message}), code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
