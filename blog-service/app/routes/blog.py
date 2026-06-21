from fastapi import APIRouter

router = APIRouter(prefix="/blogs",tags=['Blogs'])

@router.post('/add')
def add_blog():
    pass

@router.delete('/{id_blog}/delete')
def delete_blog(id_blog:int):
    pass

@router.put('/{id_blog}/update')
def update_blog(id_blog:int):
    pass

@router.get('/{id_blog}')
def get_blog(id_blog:int):
    pass

@router.get('/')
def get_all_blogs():
    pass