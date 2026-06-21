import requests

def check_user_by_id(id_user:int, user_service_url:str):
    
    response = requests.get(f"{user_service_url}/{id_user}")

    if response.status_code == 200:
        return True
    return False