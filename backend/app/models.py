from .database import base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=True)
    username = Column(String, index=True, unique=True)
    email = Column(String)
    senha = Column(String)
    favorite_artist = Column(String, nullable=True)
    
class Artist(base):
    __tablename__ = 'artist'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String)
    music_genre = Column(String)