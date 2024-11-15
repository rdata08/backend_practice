from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    assignments = db.Column(db.Array, nullable=False, default = [])
    instructors = db.Column(db.Array, nullable=False, default = [])
    students = db.Column(db.Array, nullable=False, default = [])

    def __init__(self, **kwargs):
        self.id = kwargs.get("id", "")
        self.code = kwargs.get("code", "")
        self.name = kwargs.get("name", "")
        
    def serialize(self):
        return {
            "id" : self.id,
            "code" : self.code,
            "name" : self.name
        }
    
class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable = False)
    netid = db.Column(db.String, nullable = False)
    courses = db.Column()

class Assignment(db.Model):
    __tablename__ = "assignments"
    