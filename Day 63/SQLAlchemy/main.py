from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
Writing SQL commands are complicated and error-prone. It would be much better if we could just write 
Python code and get the compiler to help us spot typos and errors in our code. That's why SQLAlchemy was created.

SQLAlchemy is defined as an ORM (Object Relational Mapping) library. This means that it's able to map the relationships 
in the database into Objects. Fields become Object properties. Tables can be defined as separate Classes and each row of
data is a new Object. This will make more sense after we write some code and see how we can create a Database/Table/Row
of data using SQLAlchemy.
"""

app = Flask(__name__)

# # CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy()
# Initialise the app with the extension
db.init_app(app)


# # CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()
"""
In addition to these things, the most crucial thing to figure out when working with any new database technology is 
how to CRUD data records.

Create.Read.Update.Delete

"""

# CREATE RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

"""
To read all the records we first need to create a "query" to select things from the database. When we execute a query 
during a database session we get back the rows in the database (a Result object). We then use scalars() to get 
the individual elements rather than entire rows.
"""
# READ RECORD
# with app.app_context():
#     result = db.session.execute(db.select(Book).order_by(Book.title))
#     all_books = result.scalars()

"""
Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use. 
Since Flask-SQLAlchemy version 3.0 the previous query methods like Book.query.get() have been deprecated
"""

# UPDATE A PARTICULAR RECORD BY QUERY
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()

# UPDATE A RECORD BY PRIMARY KEY
# book_id = 1
# with app.app_context():
#     # book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     book_to_update = db.get_or_404(Book, book_id)
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Water"
#     db.session.commit()

"""
You can also delete by querying for a particular value e.g. by title or one of the other properties. Again, 
the get_or_404() method is quite handy.
"""

# DELETE A PARTICULAR RECORD BY PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()

