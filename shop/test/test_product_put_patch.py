import requests

PRODUCT_UPDATE_URL = "http://localhost:8000/store/products/1/"

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODIxNTExLCJpYXQiOjE3MjU4MjEyMTEsImp0aSI6IjVhODkwNjM0MjQ3OTQ4NGFhNWQyN2JhNGRiMjBkZjNjIiwidXNlcl9pZCI6MX0.D4F0iiu6RN2glVtNCWwZf8JuedYBO3dCjjt__oTorWo"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

data = {
    "name": "Кроссовки Nike",
    "description": "Обновленные спортивные кроссовки для бега",
    "price": 8999,
    "category": 1
}

response = requests.put(PRODUCT_UPDATE_URL, json=data, headers=headers)

if response.status_code == 200:
    updated_product = response.json()
    print("Товар успешно обновлен!")
    print(f"Обновленные данные о товаре: {updated_product}")
else:
    print(f"Ошибка при обновлении товара. Статус код: {response.status_code}")
    print(f"Ответ от сервера: {response.json()}")
