from config import db

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    contact_number = db.Column(db.String(20))
    address = db.Column(db.Text)
    role = db.Column(db.Enum('Admin', 'Customer'), default='Customer')
