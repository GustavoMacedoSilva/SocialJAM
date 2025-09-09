from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import Optional
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter()

@router.post('/artistCreate', status_code=status.HTTP_201_CREATED, tags=['Artist'])
def createArtist(request:schemas.Artist, db:Session=Depends(get_db)):
    new_artist=models.Artist(
        nome = request.nome,
        music_genre=request.music_genre
    )
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)
    return new_artist

@router.get("/artistAll",response_model=List[schemas.Artist], tags=['Artist'])
def showAllArtists(db:Session=Depends(get_db)):
    artists = db.query(models.Artist).all()
    return artists

@router.get("/artist/{nome}", status_code=status.HTTP_200_OK, response_model=List[schemas.ShowArtist], tags=['Artist'])
def showArtist(nome, response:Response, limit: Optional[int] = None, db:Session=Depends(get_db)):
    query = db.query(models.Artist).filter(models.Artist.nome==nome)
    if limit:
        query = query.limit(limit)
    artists = query.all()
    if not artists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nao existe esse Artista")
    return artists