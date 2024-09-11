import os
import requests
from dotenv import load_dotenv

# Получаем значения из .env файла
load_dotenv()
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
REPO_NAME = os.getenv('REPO_NAME')

BASE_URL = "https://api.github.com"
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Создание репозитория
def create_repo():
    url = f"{BASE_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "auto_init": True,
        "private": False  # создаем публичный репозиторий
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Репозиторий '{REPO_NAME}' успешно создан.")
    else:
        print(f"Ошибка при создании репозитория: {response.json()}")

# Проверка на наличие
def check_repo_exists():
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"Репозиторий '{REPO_NAME}' существует.")
    else:
        print(f"Репозиторий '{REPO_NAME}' не найден.")

# Удаление репозитория
def delete_repo():
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{REPO_NAME}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Репозиторий '{REPO_NAME}' успешно удален.")
    else:
        print(f"Ошибка при удалении репозитория: {response.json()}")

if __name__ == "__main__":
    create_repo()
    check_repo_exists()
    delete_repo()
