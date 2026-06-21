from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from app.services.db import database, Session
from app.schemas.user import User

router = APIRouter(prefix="/users",tags=['Users'])

@router.post('/add', response_model=User)
def add_user(user:User, session:Session = Depends(database.get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)

    return user

@router.delete('/{id_user}/delete', response_model=User)
def delete_user(id_user:int, session:Session = Depends(database.get_session)):
    user = session.get(User, id_user)
    if not user:
        raise HTTPException(status_code=404, detail="user not found!")
    
    session.delete(user)
    session.commit()

    return user

@router.put('/{id_user}/update', response_model=User)
def update_user(id_user:int, user_data:User, session:Session = Depends(database.get_session)):
    user = session.get(User, id_user)
    if not user:
        raise HTTPException(status_code=404, detail="user not found!")
    
    for field, value in user_data.model_dump().items():
        setattr(user, field, value)

    session.commit()
    session.refresh(user)
    return user

@router.get('/{id_user}', response_model=User)
def get_user(id_user:int, session:Session = Depends(database.get_session)):
    user = session.get(User, id_user)
    if not user:
        raise HTTPException(status_code=404, detail="user not found!")
    
    return user

@router.get('/', response_model=List[User])
def get_all_users(skip:int = 0, limit:int = 10, session:Session = Depends(database.get_session)):
    users = session.exec(select(User).offset(skip).limit(limit)).all()
    return users