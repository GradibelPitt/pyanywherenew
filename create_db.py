"""
Database initialization script.
Creates the SQLite database and tables.
"""
import sys
import os

# Add the Models_skeleton directory to path to import the model
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '09 - Models_skeleton'))

from sqlalchemy import create_engine
from models import Base

# Create database engine
db_path = os.path.join(os.path.dirname(__file__), 'users.db')
engine = create_engine(f'sqlite:///{db_path}', echo=True)

# Create all tables
Base.metadata.create_all(bind=engine)

print(f"\nDatabase initialized successfully at: {db_path}")
print("Tables created: users")
