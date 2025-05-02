import requests
from src.app.details.config.config import integration_config


def get_user(user_id: int):
    response = requests.get(f"{integration_config.user_service_url}/api/users/?id={user_id}")
    return response.json()


def check_user_exists(user_id: int):
    response = requests.get(f"{integration_config.user_service_url}/api/users/?id={user_id}")
    if response.status_code != 404:
        return True
    return False
