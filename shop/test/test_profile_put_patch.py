import requests

PROFILE_UPDATE_URL = "http://localhost:8000/store/profiles/1/"

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODc3NjkwLCJpYXQiOjE3MjU4NzczOTAsImp0aSI6IjY5MGRjN2JkMGIzNTQ0OWI4NzEyZDBjNGVjYTJkZmIzIiwidXNlcl9pZCI6Mn0.muHLWTosYy_JI_uiDAqvta8pwwN3rwiszCs8hBpbpYk"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "phone_number": "+996555123457",
    "address": "г. Бишкек, ул. Советская, 123",
}


response = requests.put(PROFILE_UPDATE_URL, json=data, headers=headers)


if response.status_code == 200:
    updated_profile = response.json()
    print("Профиль успешно обновлен!")
    print(f"Обновленные данные профиля: {updated_profile}")
else:
    print(f"Ошибка при обновлении профиля. Статус код: {response.status_code}")
    print(f"Ответ от сервера: {response.json()}")
