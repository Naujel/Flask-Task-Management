from database.db import db
from datetime import datetime

class Task(db.Model):
    id = db.Column(db.String(64), primary_key=True, unique=True)
    task_name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(300))
    date = db.Column(db.String(50), default=None)

    def __init__(self, id, task_name, description, date):
        self.id = id
        self.task_name = task_name
        self.description = description
        self.date = datetime.strftime(date, "%d-%m-%y")