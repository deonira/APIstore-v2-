import requests

TOKEN_URL = "http://localhost:8000/api/token/"

data = {
    "username": "newuser",
    "password": "password123"
}

response = requests.post(TOKEN_URL, data=data)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data.get("access")
    refresh_token = token_data.get("refresh")
    print("Авторизация успешна!")
    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")
else:
    print(f"Ошибка авторизации. Статус код: {response.status_code}")
    print(f"Ответ от сервера: {response.json()}")