# CREATE A NEW DATABASE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CREATE A NEW TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # OPTIONAL: This allows the book object to be identified by it's title if printed
    def __repr__(self):
        return f"<Book {self.title}>"

db.create_all()

# CREATE A NEW RECORD (id field is auto generated)
# new_book = Book(title="Neuromancer", author="William Gibson", rating=8.7)
# db.session.add(new_book)
# db.session.commit()

# READ ALL RECORDS
# all_books = db.session.query(Book).all()
# print(all_books)

# READ A PARTICULAR RECORD BY QUERY
# book = Book.query.filter_by(title="Neuromancer").first()
# print(book)

# UPDATE A PARTICULAR RECORD BY QUERY
# book_to_update = Book.query.filter_by(title='Neuromancer').first()
# book_to_update.title = "Count Zero"
# db.session.commit()

# UPDATE A RECORD BY PRIMARY KEY
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Mona Lisa Overdrive"
# db.session.commit()

# DELETE A PARTICULAR RECORD BY PRIMARY KEY
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()





if __name__ == "__main__":
    app.run(debug=True)