from flask import Flask
from extensions import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///songs.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Turning off old, extra feature: for performance and console cleanup
app.config["JSON_COMPACT"] = False # For debugging purposes

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'You are home.'


if __name__ == '__main__':
    app.run(debug=True)

