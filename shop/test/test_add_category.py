import requests

ADD_CATEGORY_URL = "http://localhost:8000/api/categories/"

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODIxNTExLCJpYXQiOjE3MjU4MjEyMTEsImp0aSI6IjVhODkwNjM0MjQ3OTQ4NGFhNWQyN2JhNGRiMjBkZjNjIiwidXNlcl9pZCI6MX0.D4F0iiu6RN2glVtNCWwZf8JuedYBO3dCjjt__oTorWo"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "name": "Обувь",
    "description": "Категория для спортивной и повседневной обуви"
}

response = requests.post(ADD_CATEGORY_URL, json=data, headers=headers)

if response.status_code == 201:
    print("Категория успешно добавлена!")
    print(f"Ответ от сервера: {response.json()}")
else:
    print(f"Ошибка при добавлении категории. Статус код: {response.status_code}")
    print(f"Ответ от сервера: {response.json()}")
