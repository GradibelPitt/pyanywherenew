# Lab Requirements Verification Document

## Overview
This document verifies that the implementation in PR #2 (branch `copilot/add-user-model-and-registration`) fully meets all the laboratory requirements outlined in the PDF specification.

## Requirements Verification

### 1. ✅ User Model (Database Model)

**Requirement**: Create a User model with only the fields: `id`, `username`, `password`

**Implementation**: `09 - Models_skeleton/models.py`

```python
class User(Base):
    __tablename__ = "users"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
```

**Verification**: ✅ PASS
- Model defines exactly three fields: `id`, `username`, `password`
- Uses SQLAlchemy with `declarative_base()`
- `id` is auto-incrementing primary key
- `username` is unique and not nullable
- `password` is not nullable
- Located in correct path: `09 - Models_skeleton/models.py`

### 2. ✅ Login Route and Users Dictionary Reconstruction

**Requirement**: In the login route, read all users from the database and reconstruct the users dict exactly as the original fake dictionary so existing login logic can be reused.

**Implementation**: `run.py` lines 38-44

```python
# Query database and reconstruct users dict as required by lab
db_session = Session()
try:
    db_users = db_session.query(User).all()
    users = {user.username: user.password for user in db_users}
finally:
    db_session.close()
```

**Verification**: ✅ PASS
- Login route queries all users from database
- Reconstructs users dict using dictionary comprehension: `{user.username: user.password for user in db_users}`
- This matches the exact structure required: `users = {username: password}`
- Reuses original login logic: `if username in users and users[username] == password`
- Proper database session management with try/finally

### 3. ✅ Login Page Modification

**Requirement**: Modify `templates/login.html` to include the text: "Do not have an account? Register" where Register is an anchor link to `/register`.

**Implementation**: `templates/login.html` lines 26-28

```html
<div class="link">
    <p>Do not have an account? <a href="{{ url_for('register') }}">Register</a></p>
</div>
```

**Verification**: ✅ PASS
- Contains exact text: "Do not have an account? Register"
- "Register" is an anchor link (`<a>` tag)
- Links to `/register` route using `url_for('register')`
- Positioned below the login form

### 4. ✅ Registration Page

**Requirement**: Create `templates/register.html` with:
- Username input
- Password input  
- Register button
- Link back to Login page

**Implementation**: `templates/register.html`

```html
<form method="POST" action="{{ url_for('register') }}">
    <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
    </div>
    
    <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
    </div>
    
    <button type="submit">Register</button>
</form>

<div class="link">
    <p>Already have an account? <a href="{{ url_for('login') }}">Login</a></p>
</div>
```

**Verification**: ✅ PASS
- ✅ Username input field present
- ✅ Password input field present
- ✅ Register button present
- ✅ Link back to Login page present

### 5. ✅ Registration Route

**Requirement**: Create `/register` route:
- GET: shows registration form
- POST: saves user to database and redirects to `/login`

**Implementation**: `run.py` lines 56-88

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
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
```

**Verification**: ✅ PASS
- ✅ GET request shows registration form
- ✅ POST request processes registration
- ✅ Validates username and password are not empty
- ✅ Checks for duplicate usernames
- ✅ Creates new User instance with username and password
- ✅ Commits to database with proper error handling
- ✅ Redirects to login page after successful registration: `redirect(url_for('login'))`

### 6. ✅ Registration Flow

**Requirement**: After registration, user should jump to login page, then login.

**Implementation**: `run.py` line 81

```python
return redirect(url_for('login'))
```

**Verification**: ✅ PASS
- After successful registration, user is redirected to login page
- User can then login with newly created credentials
- Flow: Register → Login → Profile

## Additional Features (Beyond Requirements)

The implementation includes additional features that enhance the application without contradicting requirements:

1. **Profile Page** (`templates/profile.html`)
   - Session-protected route
   - Displays logged-in username
   - Provides logout functionality

2. **Logout Route** (`/logout`)
   - Clears user session
   - Redirects to login page

3. **Base Template** (`templates/base.html`)
   - Consistent styling across all pages
   - Clean, minimal design
   - Error message display support

4. **Database Initialization** (`create_db.py`)
   - Helper script to initialize SQLite database
   - Creates tables before first run

5. **Documentation** (`README.md`)
   - Comprehensive setup instructions
   - Security warnings about plaintext passwords
   - Lab requirements checklist

6. **Dependency Management** (`requirements.txt`)
   - Flask 3.0.0
   - SQLAlchemy 2.0.23

7. **Git Configuration** (`.gitignore`)
   - Excludes database files
   - Excludes Python cache
   - Excludes virtual environments

## Security Considerations

**Note**: The implementation intentionally uses plaintext password storage to maintain compatibility with the lab's existing login logic that expects a plain users dictionary. This is documented in:

- `README.md` (lines 67-73): Clear security warning
- `09 - Models_skeleton/models.py` (line 3): Comment about plaintext passwords
- `run.py` (line 108-109): Comment about debug mode

The README explicitly states:
> **⚠️ WARNING: This application has the following security considerations:**
> 
> 1. **Plaintext Passwords**: Passwords are stored in plaintext in the database. This is intentionally done for lab compatibility purposes...
> 
> **DO NOT use this code in production without implementing proper security measures!**

## Code Quality

- Clean, readable code structure
- Proper comments explaining key sections
- Consistent naming conventions
- Error handling in database operations
- Resource management (database sessions properly closed)
- Follows Flask best practices
- Modular design with blueprints-ready structure

## Conclusion

**Status**: ✅ **ALL REQUIREMENTS MET**

The implementation in PR #2 (`copilot/add-user-model-and-registration`) fully satisfies all laboratory requirements:

1. ✅ User model with id, username, password
2. ✅ Login route reconstructs users dictionary from database
3. ✅ Login page contains "Do not have an account? Register" link
4. ✅ Register page with all required form elements
5. ✅ Register route handles GET/POST and redirects to login
6. ✅ Complete registration → login → profile flow

The code is well-documented, includes proper security warnings, and provides a complete, functional web application that meets all specified requirements while maintaining lab compatibility.

**Recommendation**: This implementation is ready for submission and fully completes the laboratory assignment.
