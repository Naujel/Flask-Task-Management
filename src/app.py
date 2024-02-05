from flask import Flask
from decouple import config
from config import config
from flask_sqlalchemy import SQLAlchemy
from routes.tasks import main
from database.db import db

app = Flask(__name__)
app.config.from_object(config['config'])

with app.app_context():
    db.init_app(app)
    db.create_all()

if __name__ == '__main__':
    app.register_blueprint(main, url_prefix='/tasks/')
    app.run()