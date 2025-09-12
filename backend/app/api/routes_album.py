from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import Optional
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter()

@router.post('/albumCreate',status_code=status.HTTP_201_CREATED, tags=['Album'])
def createAlbum(request:schemas.Album, db:Session=Depends(get_db)):
    new_album = models.Album(
        nome=request.nome,
        total_tracks=request.total_tracks,
        artist_id = request.artist_id
    )
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    return new_album

@router.get("/album/{nome}", status_code=status.HTTP_200_OK, response_model=List[schemas.Album], tags=['Album'])
def showArtist(nome, response:Response, limit:Optional[int] = None, db:Session=Depends(get_db)):
    query = db.query(models.Album).filter(models.Album.nome==nome)
    if limit:
        query = query.limit(limit)
    albums = query.all()
    if not albums:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nao existe esse Album")
    return albums