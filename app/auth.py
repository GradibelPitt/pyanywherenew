"""Authentication routes and views."""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User
import re

auth_bp = Blueprint('auth', __name__)


def validate_email(email):
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password(password):
    """Validate password strength (minimum 6 characters)."""
    return len(password) >= 6


@auth_bp.route('/')
def index():
    """Home page."""
    return render_template('index.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration."""
    if current_user.is_authenticated:
        return redirect(url_for('auth.profile'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        # Validation
        errors = []
        
        if not username or len(username) < 3:
            errors.append('Username must be at least 3 characters long.')
        
        if not email or not validate_email(email):
            errors.append('Please provide a valid email address.')
        
        if not password or not validate_password(password):
            errors.append('Password must be at least 6 characters long.')
        
        if password != confirm_password:
            errors.append('Passwords do not match.')
        
        # Check if user already exists
        if not errors:
            if User.query.filter_by(username=username).first():
                errors.append('Username already exists.')
            
            if User.query.filter_by(email=email).first():
                errors.append('Email already registered.')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('register.html', 
                                   username=username, 
                                   email=email)
        
        # Create new user
        user = User(username=username, email=email)
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration. Please try again.', 'error')
            return render_template('register.html', 
                                   username=username, 
                                   email=email)
    
    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User login."""
    if current_user.is_authenticated:
        return redirect(url_for('auth.profile'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember', False) == 'on'
        
        if not username or not password:
            flash('Please provide both username and password.', 'error')
            return render_template('login.html', username=username)
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user, remember=remember)
            flash(f'Welcome back, {user.username}!', 'success')
            
            # Redirect to next page or profile
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            return redirect(url_for('auth.profile'))
        else:
            flash('Invalid username or password.', 'error')
            return render_template('login.html', username=username)
    
    return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    """User logout."""
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.index'))


@auth_bp.route('/profile')
@login_required
def profile():
    """User profile page (protected route)."""
    return render_template('profile.html', user=current_user)
