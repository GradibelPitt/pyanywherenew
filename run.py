"""
Flask application with user authentication and registration.
"""
import sys
import os

# Add the '09 - Models_skeleton' directory to sys.path to import models
models_dir = os.path.join(os.path.dirname(__file__), '09 - Models_skeleton')
sys.path.insert(0, models_dir)

from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a random secret key

# Database setup
engine = create_engine("sqlite:///users.db", echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


@app.route('/')
def index():
    """Redirect to login page."""
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login route: GET shows form, POST authenticates user."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Query database and reconstruct users dict as required by lab
        db_session = Session()
        try:
            db_users = db_session.query(User).all()
            users = {user.username: user.password for user in db_users}
        finally:
            db_session.close()
        
        # Original login logic using reconstructed users dict
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('profile'))
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register route: GET shows form, POST creates new user."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validate input
        if not username or not password:
            return render_template('register.html', error='Username and password are required')
        
        # Create new user
        db_session = Session()
        try:
            # Check if username already exists
            existing_user = db_session.query(User).filter_by(username=username).first()
            if existing_user:
                return render_template('register.html', error='Username already exists')
            
            # Add new user to database
            new_user = User(username=username, password=password)
            db_session.add(new_user)
            db_session.commit()
            
            # Redirect to login after successful registration
            return redirect(url_for('login'))
        except Exception as e:
            db_session.rollback()
            return render_template('register.html', error='Error creating user')
        finally:
            db_session.close()
    
    return render_template('register.html')


@app.route('/profile')
def profile():
    """Profile route: protected by session check."""
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('profile.html', username=session['username'])


@app.route('/logout')
def logout():
    """Logout route: clear session and redirect to login."""
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
