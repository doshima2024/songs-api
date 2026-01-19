from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///songs.db"
app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False # Turning off old, extra feature: for performance and console cleanup
app.config["JSON_COMPACT"] = False # For debugging purposes

db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'You are home.'


if __name__ == '__main__':
    app.run(debug=True)