# Flask Authentication App

A minimal but complete Flask-based authentication system with user registration, login, logout, and session management.

## Features

- 🔐 **Secure Authentication**: Password hashing with Werkzeug security
- 👤 **User Management**: Register, login, and manage user sessions
- 🛡️ **Protected Routes**: Access control for authenticated users only
- 💾 **SQLite Database**: Persistent user data with SQLAlchemy and Flask-Login
- ✅ **Form Validation**: Basic validation to ensure data integrity
- 🎨 **Responsive UI**: Clean, minimal design that works on all devices
- 🧪 **Comprehensive Tests**: Unit tests for authentication flow using pytest

## Project Structure

```
pyanywherenew/
├── app/
│   ├── __init__.py          # Flask app factory and configuration
│   ├── models.py            # User model with SQLAlchemy
│   ├── auth.py              # Authentication routes (register/login/logout/profile)
│   ├── static/
│   │   └── css/
│   │       └── style.css    # Application styles
│   └── templates/
│       ├── base.html        # Base template
│       ├── index.html       # Home page
│       ├── register.html    # Registration form
│       ├── login.html       # Login form
│       └── profile.html     # User profile page
├── tests/
│   ├── __init__.py
│   └── test_auth.py         # Authentication tests
├── run.py                   # Entry point to run the app
├── create_db.py             # Database initialization script
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies (includes pytest)
├── .env.example             # Example environment variables
├── .gitignore               # Git ignore file
└── README.md                # This file
```

## Requirements

- Python 3.8+
- pip (Python package installer)

## Installation

1. **Clone the repository** (if not already cloned):
   ```bash
   git clone https://github.com/GradibelPitt/pyanywherenew.git
   cd pyanywherenew
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables** (optional but recommended):
   ```bash
   cp .env.example .env
   # Edit .env and set your SECRET_KEY
   ```

6. **Initialize the database**:
   ```bash
   python create_db.py
   ```

## Running the Application

1. **Start the Flask development server**:
   ```bash
   python run.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Register a new user**:
   - Click "Register" or navigate to http://localhost:5000/register
   - Fill in the registration form
   - Submit to create your account

4. **Login**:
   - Navigate to http://localhost:5000/login
   - Enter your username and password
   - Click "Login"

5. **Access your profile**:
   - After logging in, you'll be redirected to your profile page
   - Or navigate to http://localhost:5000/profile

## Running Tests

1. **Install development dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Run all tests**:
   ```bash
   pytest
   ```

3. **Run tests with verbose output**:
   ```bash
   pytest -v
   ```

4. **Run tests with coverage**:
   ```bash
   pytest --cov=app tests/
   ```

## API Routes

| Route | Method | Description | Authentication Required |
|-------|--------|-------------|------------------------|
| `/` | GET | Home page | No |
| `/register` | GET, POST | User registration | No |
| `/login` | GET, POST | User login | No |
| `/logout` | GET | User logout | Yes |
| `/profile` | GET | User profile | Yes |

## Security Features

- **Password Hashing**: All passwords are hashed using Werkzeug's `generate_password_hash` before storage
- **No Plaintext Passwords**: Passwords are never stored in plaintext
- **Session Management**: Flask-Login handles secure session management
- **Protected Routes**: The `/profile` route requires authentication
- **CSRF Protection**: Built-in with Flask's session management
- **Input Validation**: Basic validation on registration and login forms
- **Debug Mode Control**: Debug mode is disabled by default in production for security

## User Model

The `User` model includes the following fields:

- `id`: Primary key (auto-generated)
- `username`: Unique username (3+ characters)
- `email`: Unique email address
- `password_hash`: Hashed password
- `created_at`: Timestamp of account creation

## Configuration

The app uses environment variables for configuration:

- `SECRET_KEY`: Secret key for session management (set in `.env` or environment)
- `FLASK_DEBUG`: Enable debug mode for development (set to `True` in `.env`, default is `False` for security)
- `SQLALCHEMY_DATABASE_URI`: Database connection string (defaults to `sqlite:///auth.db`)

## Development

To contribute or modify the application:

1. Create a new branch for your feature
2. Make your changes
3. Run tests to ensure everything works
4. Submit a pull request

## Testing Coverage

The test suite includes:

- User model tests (password hashing, user creation)
- Registration tests (successful registration, validation, duplicates)
- Login tests (successful login, wrong password, non-existent user)
- Access control tests (protected routes)
- Logout tests
- Redirect after login tests

## Troubleshooting

### Port already in use
If port 5000 is already in use, modify `run.py` to use a different port:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Database issues
If you encounter database issues, delete the `auth.db` file and run:
```bash
python create_db.py
```

### Module not found errors
Ensure your virtual environment is activated and all dependencies are installed:
```bash
pip install -r requirements.txt
```

## License

This project is for educational purposes.

## Author

Built as part of the PyAnywhere project.
