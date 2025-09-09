from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import models, schemas
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from ..core.security import HashPWD


router = APIRouter()


@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['User'])
def createUser(request_user:schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(
        nome=request_user.nome,
        username=request_user.username,
        email=request_user.email,
        senha=HashPWD(request_user.senha)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/user/{username}/delete', status_code=status.HTTP_204_NO_CONTENT, tags=['User'])
def delete_user(username, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==username)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario nao encontrado")
    user.delete(synchronize_session=False)
    db.commit()
    return f"{username} deletado"
    
@router.put('/user/{username}/update', status_code=status.HTTP_202_ACCEPTED, tags=['User'])
def update_user(username, request:schemas.User, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==username)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {username} não foi encontrado")
    user.update(request.model_dump(exclude_unset=True))
    db.commit()
    return "User Updated"

@router.get('/user', response_model=List[schemas.ShowUser], tags=['User'])
def get_all_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get('/user/{username}', status_code=200, response_model=schemas.ShowUser, tags=['User'])
def show_user(username,response:Response, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe usuário {username}')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Não existe usuário {username}'}
    return user