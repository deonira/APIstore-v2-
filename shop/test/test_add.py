import requests

ADD_PRODUCT_URL = "http://localhost:8000/store/products/"

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODIxNTExLCJpYXQiOjE3MjU4MjEyMTEsImp0aSI6IjVhODkwNjM0MjQ3OTQ4NGFhNWQyN2JhNGRiMjBkZjNjIiwidXNlcl9pZCI6MX0.D4F0iiu6RN2glVtNCWwZf8JuedYBO3dCjjt__oTorWo"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "name": "Кроссовки Adidas",
    "description": "Спортивные кроссовки для бега",
    "price": 7999,
    "category": 1
}

response = requests.post(ADD_PRODUCT_URL, json=data, headers=headers)

if response.status_code == 201:
    print("Товар успешно добавлен!")
    print(f"Ответ от сервера: {response.json()}")
else:
    print(f"Ошибка при добавлении товара. Статус код: {response.status_code}")
    print(f"Ответ от сервера: {response.json()}")
