from extensions import db

class Category(db.Model):
    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return f"<Category {self.category_name}>"

    def to_dict(self):
        return {
            "category_id": self.category_id,    
            "category_name": self.category_name,
            "description": self.description
        }
