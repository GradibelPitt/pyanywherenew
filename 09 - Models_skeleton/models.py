"""
User model for the application using SQLAlchemy.
This model stores users with plaintext passwords for lab compatibility.
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """User model with id, username, and password fields."""
    
    __tablename__ = "users"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String, nullable=False, unique=True)
    password = Column("password", String, nullable=False)
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"
