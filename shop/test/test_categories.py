import requests
CATEGORY_URL = "http://localhost:8000/store/categories/"
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODc3ODAzLCJpYXQiOjE3MjU4Nzc1MDMsImp0aSI6ImU5YWU3YmNmYmFhYTQ0NGY4ODc5NmJlNDYxOTUyNGQ2IiwidXNlcl9pZCI6MX0.4Cu_akmEgaLT708Hu-vDdfh_WO_z6xWu48M0kWpPuA8"

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
