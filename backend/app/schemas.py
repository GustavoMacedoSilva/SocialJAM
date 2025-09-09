from typing import Optional, List
from pydantic import BaseModel

class User(BaseModel):
    username: str
    nome: Optional[str] = None
    senha: str
    email: str
    
class ShowUser(BaseModel):
    username: str
    nome: str
    email: str
    class Config:
        orm_mode = True
    
class Artist(BaseModel):
    nome: str
    music_genre: str
    
class ShowArtist(Artist):
    class Config:
        orm_mode = True