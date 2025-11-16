"""
Helper script to initialize the SQLite database and create tables.
Run this script once before starting the Flask application.
"""
import sys
import os

# Add the '09 - Models_skeleton' directory to sys.path to import models
models_dir = os.path.join(os.path.dirname(__file__), '09 - Models_skeleton')
sys.path.insert(0, models_dir)

from sqlalchemy import create_engine
from models import Base

# Create the database engine
engine = create_engine("sqlite:///users.db", echo=True)

# Create all tables
Base.metadata.create_all(bind=engine)

print("\nDatabase initialized successfully!")
print("Tables created: users")
