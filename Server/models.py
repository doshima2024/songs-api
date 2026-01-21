from extensions import db 

class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    clone_count = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, name, rating=0, clone_count=0):
        self.name = name
        self.rating=rating
        self.clone_count = clone_count

    def __repr__(self):
        return f"<Song with ID: {self.id} is called {self.name}, has a rating of {self.rating} and has been cloned {self.clone_count} times>"
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'rating': self.rating, 'clone_count': self.clone_count }