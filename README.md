# PyAnywhere Lab - User Authentication System

This repository contains a Flask-based user authentication system created for lab exercises.

## Features

- User registration with username and password
- User login with session management
- Protected profile page
- User logout functionality
- SQLite database for user storage

## Project Structure

```
pyanywherenew/
├── 09 - Models_skeleton/
│   └── models.py              # SQLAlchemy User model
├── templates/
│   ├── login.html             # Login page with link to register
│   ├── register.html          # Registration page with link to login
│   └── profile.html           # User profile page (protected)
├── create_db.py               # Database initialization script
├── run.py                     # Flask application with routes
└── README.md                  # This file
```

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GradibelPitt/pyanywherenew.git
   cd pyanywherenew
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install required packages:**
   ```bash
   pip install flask flask-sqlalchemy
   ```

5. **Initialize the database:**
   ```bash
   python create_db.py
   ```
   This will create a `users.db` file in the project root.

## Running the Application

1. **Start the Flask application:**
   ```bash
   python run.py
   ```

2. **Access the application:**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. **Using the application:**
   - You will be redirected to the login page
   - Click "Register" to create a new account
   - After registration, you'll be redirected back to login
   - Log in with your credentials
   - View your profile page
   - Click "Logout" to end your session

## Routes

- `/` - Root route (redirects to login)
- `/login` - Login page (GET to display, POST to authenticate)
- `/register` - Registration page (GET to display, POST to create user)
- `/profile` - User profile page (requires active session)
- `/logout` - Logout route (clears session and redirects to login)

## Database Schema

### User Model

The User model is defined in `09 - Models_skeleton/models.py` with the following fields:

- `id` (Integer, Primary Key, Auto-increment)
- `username` (String, Unique, Not Null)
- `password` (String, Not Null)

## Security Note ⚠️

**IMPORTANT: This application has several security limitations intentional for lab purposes:**

1. **Plaintext Passwords**: Passwords are stored in plaintext in the database. This is intentionally insecure and done only for lab compatibility and educational purposes. The original lab code used a simple dictionary with plaintext passwords, and this implementation maintains that behavior to demonstrate database integration without introducing additional complexity.

2. **Debug Mode Enabled**: The Flask application runs with `debug=True` for easier development and learning. This should be disabled in production as it can allow attackers to run arbitrary code through the debugger.

3. **Hardcoded Secret Key**: The session secret key is hardcoded. In production, use a secure, randomly generated secret key stored in environment variables.

**In a production environment, you should NEVER:**
- Store passwords in plaintext - always use proper password hashing libraries such as:
  - `werkzeug.security` (built into Flask)
  - `bcrypt`
  - `argon2`
- Run Flask with `debug=True`
- Use hardcoded secret keys

Example of secure password handling:
```python
from werkzeug.security import generate_password_hash, check_password_hash

# When storing:
hashed_password = generate_password_hash(password)

# When verifying:
check_password_hash(hashed_password, password)
```

## Development Notes

- The application uses Flask's session management for user authentication
- The database is automatically created if it doesn't exist when running `run.py`
- Debug mode is enabled by default (should be disabled in production)
- The secret key in `run.py` should be changed to a secure random value in production

## Troubleshooting

### Import Error for models.py

If you encounter an import error related to the `09 - Models_skeleton` directory (which contains a space), the application automatically adds this directory to `sys.path`. This is handled in both `run.py` and `create_db.py`.

### Database Not Found

If you see database-related errors, make sure you've run the `create_db.py` script first:
```bash
python create_db.py
```

### Port Already in Use

If port 5000 is already in use, you can specify a different port:
```python
# In run.py, change the last line to:
app.run(debug=True, port=5001)
```

## License

This project is created for educational purposes as part of CS-1520 coursework.
