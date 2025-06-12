#📚 Flask Book Library API
A simple, RESTful API built with Flask that enables users to register, log in, and manage a personal library of books. This API supports full CRUD operations for books and uses session-based authentication via Flask-Login (no JWT required). Designed for simplicity, extensibility, and educational use.

##🚀 Features
- Authentication
- User registration and login
- Secure, session-based login with Flask-Login (no JWTs)
- Session management via cookies
- Book Management (CRUD)
- Add a new book
- Edit an existing book
- Delete a book
- Fetch all books

##🧪 Developer Extras
- Optional auto-seeding logic for demo book data

## 🛠 Tech Stack
- Layer	Technology
- Language	Python
- Framework	Flask
- Database	SQLite
- ORM	SQLAlchemy
- Auth	Flask-Login

## 🔍 Example API Endpoints
- Method ***	Endpoint ***	Description
- POST	/register	Register a new user
- POST	/login	Log in a user
- GET	/books	Fetch all books
- POST	/books	Add a new book
- PUT	/books/<book_id>	Edit an existing book
- DELETE	/books/<book_id>	Delete a book

- All book routes require an authenticated session.

##📌 Notes
- Admin privileges are not required; users can manage their own sessions.
- No frontend is included — this is an API-only project.
- Can be extended easily with JWTs, user roles, or a frontend in React/Vue.
