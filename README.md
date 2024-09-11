# GitHub API Test

## Описание
Тест умеет создавать, проверять наличие и удалять репозиторий на GitHub.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone <URL репозитория>
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd github_api_test
    ```

3. Создайте виртуальное окружение (опционально):

    ```bash
    python -m venv venv
    source venv/bin/activate  # для Windows используйте venv\Scripts\activate
    ```

4. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

5. Создайте файл `.env` в корне проекта и добавьте туда ваши данные:

    ```plaintext
    GITHUB_TOKEN=your_github_token
    GITHUB_USERNAME=your_github_username
    REPO_NAME=test_repo
    ```

## Запуск теста

1. Убедитесь, что все зависимости установлены и файл `.env` заполнен.
2. Запустите скрипт:

    ```bash
    python test_api.py
    ```

## Ожидаемый результат

Скрипт создаст новый публичный репозиторий с указанным именем, проверит его наличие, а затем удалит.
