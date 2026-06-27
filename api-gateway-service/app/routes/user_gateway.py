import httpx
from fastapi import APIRouter, Request
from app.schemas.user import User
from typing import List
from app.config import config

USER_SERVICE_URL = config.USER_SERVICE_URL
PREFIX = config.HOST_URL

router = APIRouter(prefix='/users', tags=['User Service'])

@router.post('/add', response_model=User)
async def add_user(request:Request, user:User):
    endpoint = str(request.url).replace(PREFIX, '')

    async with httpx.AsyncClient() as client:
        res = await client.post(f"{USER_SERVICE_URL}{endpoint}", json=user.model_dump())
    
    return User.model_validate(res.json())


@router.delete('/{id_user}/delete', response_model=User)
async def delete_user(request:Request, id_user:int):
    endpoint = str(request.url).replace(PREFIX, '')

    async with httpx.AsyncClient() as client:
        res = await client.delete(f"{USER_SERVICE_URL}{endpoint}")
    
    return User.model_validate(res.json())

@router.put('/{id_user}/update', response_model=User)
async def update_user(request:Request, id_user:int, user_data:User):
    endpoint = str(request.url).replace(PREFIX, '')

    async with httpx.AsyncClient() as client:
        res = await client.put(f"{USER_SERVICE_URL}{endpoint}", json=user_data.model_dump())
    
    return User.model_validate(res.json())

@router.get('/{id_user}', response_model=User)
async def get_user(request:Request, id_user:int):
    endpoint = str(request.url).replace(PREFIX, '')

    async with httpx.AsyncClient() as client:
        res = await client.get(f"{USER_SERVICE_URL}{endpoint}")

    return User.model_validate(res.json())

@router.get('/', response_model=List[User])
async def get_all_users(request:Request, skip:int = 0, limit:int = 10):
    endpoint = str(request.url).replace(PREFIX, '')

    async with httpx.AsyncClient() as client:
        res = await client.get(f"{USER_SERVICE_URL}{endpoint}")

    return [User.model_validate(obj) for obj in res.json()]