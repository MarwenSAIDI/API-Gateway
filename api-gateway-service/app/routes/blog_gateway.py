import httpx
from fastapi import APIRouter, Request
from typing import List
from app.schemas.blog import Blog
from app.config import config

BLOG_SERVICE_URL = config.BLOG_SERVICE_URL
PREFIX = config.HOST_URL

router = APIRouter(prefix='/blogs', tags=['Blog Service'])

@router.post('/add', response_model=Blog)
async def add_blog(request:Request, blog:Blog):
    endpoint = str(request.url).replace(PREFIX, '')

    async with httpx.AsyncClient() as client:
        res = await client.post(f"{BLOG_SERVICE_URL}{endpoint}", json=blog.model_dump())

    return Blog.model_validate(res.json())

@router.delete('/{id_blog}/delete', response_model=Blog)
async def delete_blog(request:Request, id_blog:int):
    endpoint = str(request.url).replace(PREFIX, '')

    async with httpx.AsyncClient() as client:
        res = await client.delete(f"{BLOG_SERVICE_URL}{endpoint}")

    return Blog.model_validate(res.json())

@router.put('/{id_blog}/update', response_model=Blog)
async def update_blog(request:Request, id_blog:int, blog_data:Blog):
    endpoint = str(request.url).replace(PREFIX, '')

    async with httpx.AsyncClient() as client:
        res = await client.put(f"{BLOG_SERVICE_URL}{endpoint}", json=blog_data.model_dump())

    return Blog.model_validate(res.json())

@router.get('/{id_blog}')
async def get_blog(request:Request, id_blog:int):
    endpoint = str(request.url).replace(PREFIX, '')
    
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BLOG_SERVICE_URL}{endpoint}")

    return Blog.model_validate(res.json())

@router.get('/',response_model=List[Blog])
async def get_all_blogs(request:Request, skip:int = 0, limit:int = 10):
    print(PREFIX)
    endpoint = str(request.url).replace(PREFIX,'')

    async with httpx.AsyncClient() as client:
        res = await client.get(f"{BLOG_SERVICE_URL}{endpoint}")

    return [Blog.model_validate(obj) for obj in res.json()] 