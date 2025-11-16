"""
Flask application with user authentication.
Implements login, register, profile, and logout routes.
"""
import sys
import os

# Add the Models_skeleton directory to path to import the model
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '09 - Models_skeleton'))

from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Database setup
db_path = os.path.join(os.path.dirname(__file__), 'users.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)


@app.route('/')
def index():
    """Root route redirects to login."""
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login route.
    GET: Display login form
    POST: Verify credentials and create session
    """
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        # Query all users from database and reconstruct users dict
        db_session = Session()
        try:
            db_users = db_session.query(User).all()
            # Reconstruct users dict exactly as the original fake dictionary
            users = {user.username: user.password for user in db_users}
            
            # Existing login verification logic (reused without change)
            if username in users and users[username] == password:
                session['username'] = username
                return redirect(url_for('profile'))
            else:
                return render_template('login.html', error='Invalid username or password')
        finally:
            db_session.close()
    
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registration route.
    GET: Display registration form
    POST: Create new user and redirect to login
    """
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        if not username or not password:
            return render_template('register.html', error='Username and password are required')
        
        db_session = Session()
        try:
            # Check if username already exists
            existing_user = db_session.query(User).filter_by(username=username).first()
            if existing_user:
                return render_template('register.html', error='Username already exists')
            
            # Create new user
            new_user = User(username=username, password=password)
            db_session.add(new_user)
            db_session.commit()
            
            return redirect(url_for('login'))
        except Exception as e:
            db_session.rollback()
            return render_template('register.html', error='Error creating user')
        finally:
            db_session.close()
    
    return render_template('register.html')


@app.route('/profile')
def profile():
    """
    Profile route - protected by session check.
    Display user profile information.
    """
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('profile.html', username=session['username'])


@app.route('/logout')
def logout():
    """
    Logout route.
    Clear session and redirect to login.
    """
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
