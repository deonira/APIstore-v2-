import requests
CATEGORY_URL = "http://localhost:8000/api/categories/"
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODIxMDc5LCJpYXQiOjE3MjU4MjA3NzksImp0aSI6ImY1MDY0ZGEzNWQxZDQ0NGZiOTQ5YTNjZTcxYjc4MzdkIiwidXNlcl9pZCI6MX0.m8z5o0Q04BZGylTa8LP2CmpqN23zLuSFlqQo-cIQg7o"

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.get(CATEGORY_URL, headers=headers)

if response.status_code == 200:
    categories = response.json()
    print("Категории:")
    for category in categories:
        print(f"ID: {category['id']}, Название: {category['name']}")
else:
    print(f"Ошибка при получении категорий. Статус код: {response.status_code}")
    print(f"Ответ от сервера: {response.json()}")
