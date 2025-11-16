"""Unit tests for authentication functionality."""
import pytest
from app import create_app, db
from app.models import User


@pytest.fixture
def app():
    """Create and configure a test app instance."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create a test runner for CLI commands."""
    return app.test_cli_runner()


class TestUserModel:
    """Test User model."""
    
    def test_password_hashing(self, app):
        """Test that passwords are properly hashed."""
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('testpass123')
            
            assert user.password_hash != 'testpass123'
            assert user.check_password('testpass123')
            assert not user.check_password('wrongpassword')
    
    def test_user_creation(self, app):
        """Test user creation in database."""
        with app.app_context():
            user = User(username='newuser', email='new@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()
            
            retrieved_user = User.query.filter_by(username='newuser').first()
            assert retrieved_user is not None
            assert retrieved_user.username == 'newuser'
            assert retrieved_user.email == 'new@example.com'


class TestAuthRoutes:
    """Test authentication routes."""
    
    def test_index_page(self, client):
        """Test that index page loads."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Welcome to Flask Auth App' in response.data
    
    def test_register_page_get(self, client):
        """Test that registration page loads."""
        response = client.get('/register')
        assert response.status_code == 200
        assert b'Create an Account' in response.data
    
    def test_login_page_get(self, client):
        """Test that login page loads."""
        response = client.get('/login')
        assert response.status_code == 200
        assert b'Login' in response.data
    
    def test_successful_registration(self, client, app):
        """Test successful user registration."""
        response = client.post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Registration successful' in response.data
        
        # Verify user was created
        with app.app_context():
            user = User.query.filter_by(username='testuser').first()
            assert user is not None
            assert user.email == 'test@example.com'
    
    def test_registration_password_mismatch(self, client):
        """Test registration with mismatched passwords."""
        response = client.post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'different123'
        }, follow_redirects=True)
        
        assert b'Passwords do not match' in response.data
    
    def test_registration_duplicate_username(self, client, app):
        """Test registration with duplicate username."""
        # Create first user
        with app.app_context():
            user = User(username='testuser', email='first@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()
        
        # Try to register with same username
        response = client.post('/register', data={
            'username': 'testuser',
            'email': 'second@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }, follow_redirects=True)
        
        assert b'Username already exists' in response.data
    
    def test_registration_short_password(self, client):
        """Test registration with short password."""
        response = client.post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': '12345',
            'confirm_password': '12345'
        }, follow_redirects=True)
        
        assert b'at least 6 characters' in response.data
    
    def test_successful_login(self, client, app):
        """Test successful user login."""
        # Create a user first
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()
        
        # Attempt login
        response = client.post('/login', data={
            'username': 'testuser',
            'password': 'password123'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Welcome back' in response.data
    
    def test_login_wrong_password(self, client, app):
        """Test login with wrong password."""
        # Create a user first
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()
        
        # Attempt login with wrong password
        response = client.post('/login', data={
            'username': 'testuser',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        
        assert b'Invalid username or password' in response.data
    
    def test_login_nonexistent_user(self, client):
        """Test login with non-existent user."""
        response = client.post('/login', data={
            'username': 'nonexistent',
            'password': 'password123'
        }, follow_redirects=True)
        
        assert b'Invalid username or password' in response.data
    
    def test_profile_requires_login(self, client):
        """Test that profile page requires authentication."""
        response = client.get('/profile', follow_redirects=True)
        assert b'Please log in' in response.data or b'Login' in response.data
    
    def test_profile_access_when_logged_in(self, client, app):
        """Test that logged-in users can access profile."""
        # Create and login user
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()
        
        client.post('/login', data={
            'username': 'testuser',
            'password': 'password123'
        })
        
        response = client.get('/profile')
        assert response.status_code == 200
        assert b'User Profile' in response.data
        assert b'testuser' in response.data
    
    def test_logout(self, client, app):
        """Test user logout."""
        # Create and login user
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()
        
        client.post('/login', data={
            'username': 'testuser',
            'password': 'password123'
        })
        
        # Logout
        response = client.get('/logout', follow_redirects=True)
        assert response.status_code == 200
        assert b'logged out' in response.data
        
        # Try to access profile after logout
        response = client.get('/profile', follow_redirects=True)
        assert b'Please log in' in response.data or b'Login' in response.data
    
    def test_redirect_after_login(self, client, app):
        """Test redirect to originally requested page after login."""
        # Create user
        with app.app_context():
            user = User(username='testuser', email='test@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()
        
        # Try to access profile (redirects to login)
        client.get('/profile')
        
        # Login
        response = client.post('/login', data={
            'username': 'testuser',
            'password': 'password123'
        }, follow_redirects=True)
        
        # Should redirect to profile
        assert response.status_code == 200
