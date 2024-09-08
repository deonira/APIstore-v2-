import requests

REGISTER_URL = "http://localhost:8000/api/register/"

data = {
    "username": "newuser",
    "password": "password123",
    "email": "newuser@example.com"
}

response = requests.post(REGISTER_URL, data=data)

if response.status_code == 201:
    print("Пользователь успешно зарегистрирован!")
    print(f"Ответ от сервера: {response.json()}")
else:
    print(f"Ошибка регистрации. Статус код: {response.status_code}")
    print(f"Ответ от сервера: {response.json()}")