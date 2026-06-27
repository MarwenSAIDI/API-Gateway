from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from app.services.db import database, Session
from app.services.blog import check_user_by_id
from app.config import config
from app.schemas.blog import Blog

router = APIRouter(prefix="/blogs",tags=['Blogs'])

@router.post('/add', response_model=Blog)
def add_blog(blog:Blog, session:Session = Depends(database.get_session)):
    # check if user exists
    # if not check_user_by_id(id_user=blog.writer_id, user_service_url=config.USER_SERVICE_URL):
    #     raise HTTPException(status_code=404, detail="user not found!")
    
    session.add(blog)
    session.commit()
    session.refresh(blog)

    return blog

@router.delete('/{id_blog}/delete', response_model=Blog)
def delete_blog(id_blog:int, session:Session = Depends(database.get_session)):
    blog = session.get(Blog, id_blog)
    if not blog:
        raise HTTPException(status_code=404, detail="blog not found!")
    
    session.delete(blog)
    session.commit()

    return blog

@router.put('/{id_blog}/update', response_model=Blog)
def update_blog(id_blog:int, blog_data:Blog, session:Session = Depends(database.get_session)):
    blog = session.get(Blog, id_blog)
    if not blog:
        raise HTTPException(status_code=404, detail="blog not found!")
    
    for field, value in blog_data.model_dump().items():
        setattr(blog, field, value)

    session.commit()
    session.refresh(blog)
    return blog

@router.get('/{id_blog}', response_model=Blog)
def get_blog(id_blog:int, session:Session = Depends(database.get_session)):
    blog = session.get(Blog, id_blog)
    if not blog:
        raise HTTPException(status_code=404, detail="blog not found!")
    
    return blog

@router.get('/',response_model=List[Blog])
def get_all_blogs(skip:int = 0, limit:int = 10, session:Session = Depends(database.get_session)):
    blogs = session.exec(select(Blog).offset(skip).limit(limit)).all()
    return blogs