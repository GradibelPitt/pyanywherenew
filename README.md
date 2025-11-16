# PyAnywhere User Authentication Lab

This is a Flask application implementing user authentication and registration with SQLAlchemy and SQLite.

## Features

- User registration with username and password
- User login with session management
- Protected profile page
- SQLite database for user storage

## Setup Instructions

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**On Mac/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the Database

```bash
python create_db.py
```

This will create a `users.db` SQLite database file with the users table.

### 5. Run the Application

```bash
python run.py
```

The application will start on `http://127.0.0.1:5000/`

## Usage

1. Navigate to `http://127.0.0.1:5000/`
2. You will be redirected to the login page
3. Click "Register" to create a new account
4. Enter a username and password
5. After registration, you'll be redirected to login
6. Login with your credentials
7. You'll be taken to your profile page
8. Click "Logout" to end your session

## Important Security Note

**⚠️ WARNING: This application stores passwords in plaintext in the database.**

This is intentionally done for lab compatibility purposes to match the existing login logic that expects a plain dictionary of usernames and passwords. In a real-world application, passwords should ALWAYS be hashed using a secure hashing algorithm like bcrypt or argon2.

**DO NOT use this code in production without implementing proper password hashing!**

## File Structure

```
pyanywherenew/
├── 09 - Models_skeleton/
│   └── models.py          # SQLAlchemy User model
├── templates/
│   ├── base.html          # Base template
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   └── profile.html       # User profile page
├── create_db.py           # Database initialization script
├── run.py                 # Flask application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Lab Requirements Implemented

1. ✅ User model with id, username, password in `09 - Models_skeleton/models.py`
2. ✅ Database query reconstructs users dict: `users = {user.username: user.password for user in db_users}`
3. ✅ login.html includes "Do not have an account? Register" link
4. ✅ register.html with Username, Password inputs, Register button, and link back to Login
5. ✅ /register route: GET shows form, POST writes to DB and redirects to /login
6. ✅ /login route reads users from database and reconstructs users dict before login logic
