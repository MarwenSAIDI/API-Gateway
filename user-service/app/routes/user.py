from fastapi import APIRouter

router = APIRouter(prefix="/users",tags=['Users'])

@router.post('/add')
def add_user():
    pass

@router.delete('/{id_user}/delete')
def delete_user(id_user:int):
    pass

@router.put('/{id_user}/update')
def update_user(id_user:int):
    pass

@router.get('/{id_user}')
def get_user(id_user:int):
    pass

@router.get('/')
def get_all_users():
    pass