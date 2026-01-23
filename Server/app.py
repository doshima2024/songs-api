from flask import Flask, jsonify, request
from models import Song
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

@app.get('/songs')
def get_songs():
    try:
        songs = Song.query.all()
        return jsonify([song.to_dict() for song in songs])
    except Exception as exception:
        return jsonify({'error': str(exception)}), 500 
    
@app.post('/songs')
def create_song():
    data = request.json # parse the JSON request body into Python, in this case a Python dict
    name = data.get("name")
    rating = data.get("rating")
    clone_count = data.get("clone_count")
    
    if not name:
        return jsonify({"error": "Name is a required field"}), 400 
    if rating is None:
        return jsonify({"error": "Rating is a required field"}), 400
    
    new_entry = Song(name=name, rating=rating, clone_count=clone_count) #Create the song instance

    try:
        db.session.add(new_entry)
        db.session.commit()               
        return jsonify(new_entry.to_dict()), 201 # return JSON
    except Exception as exception:
        return ({'error adding song': str(exception)}), 500
    
@app.delete('/songs/<int:id>')
def delete_song(id):
    song_to_delete = Song.query.filter(Song.id == id).first()
    if song_to_delete is None:
        return ({"error": "No song matching the specification found"}), 404
    try:
        db.session.delete(song_to_delete)
        db.session.commit()
        return '', 204
    except Exception as exception:
        return({"error": str(exception)}), 500

if __name__ == '__main__':
    app.run(debug=True)

