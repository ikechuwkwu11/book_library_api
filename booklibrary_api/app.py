from flask import Flask,jsonify,flash,request
from models import db,User,Book
from flask_login import login_user,logout_user, LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'iyke'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_library_api.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def seed_books():
    if Book.query.count() == 0:
        books = [
            Book(name="The Great Gatsby", title="Classic Novel", author="F. Scott Fitzgerald", year=1925),
            Book(name="To Kill a Mockingbird", title="Pulitzer Prize Winner", author="Harper Lee", year=1960),
            Book(name="1984", title="Dystopian Fiction", author="George Orwell", year=1949)
        ]
        db.session.bulk_save_objects(books)
        db.session.commit()


@app.route('/api/books',methods=['GET'])
def get_books():
    books = Book.query.all()
    # books_data = [{"id": book.id, "name": book.name, "title": book.title, "author": book.author, "year": book.year} for
    #               book in books]
    # books = [
    #     Book(name="The Great Gatsby", title="Classic Novel", author="F. Scott Fitzgerald", year=1925),
    #     Book(name="To Kill a Mockingbird", title="Pulitzer Prize Winner", author="Harper Lee", year=1960),
    #     Book(name="1984", title="Dystopian Fiction", author="George Orwell", year=1949)
    # ]
    # db.session.bulk_save_objects(books)
    # db.session.commit()

    books_data = [book.to_dict() for book in books ]

    return jsonify({"books":books_data}),200

@app.route('/api/register',methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"message":"Username and password are required"}),400

    new_user = User(username=username,password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"User has successfully registered. Now login!"}),201

@app.route('/api/login',methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    username = data.get('username')
    password =data.get('password')

    if not username or not password:
        return jsonify({"message":"username and password required"}), 400

    user = User.query.filter_by(username = username).first()
    if user and user.password == password:
        login_user(user)
        db.session.commit()
        return jsonify({"message":"login successful"}),201
    return jsonify({"message":"invalid user"}), 400

@app.route('/api/logout',methods = ['GET'])
def logout():
    logout_user()
    return jsonify({"message":"logged out"}),200

@app.route('/api/books',methods = ['POST'])
def add_books():
    data = request.get_json()
    name = data.get('name')
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')

    if not name or not title or not author or not year:
        return jsonify({"message":"All fields are required"}), 400

    new_user = Book(name = name, title = title, author = author, year = year)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"book has been added!"}),200

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def edit_books(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.name = data.get("name",book.name)
    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.year = data.get("year",book.year)
    db.session.commit()
    return jsonify({"message":"book has been updated"}), 200

@app.route('/api/books/<int:book_id>', methods = ['DELETE'])
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message":"Book Deleted!"}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)