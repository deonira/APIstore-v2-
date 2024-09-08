import requests
PRODUCT_DETAIL_URL = "http://localhost:8000/api/products/1/"

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODIxNTExLCJpYXQiOjE3MjU4MjEyMTEsImp0aSI6IjVhODkwNjM0MjQ3OTQ4NGFhNWQyN2JhNGRiMjBkZjNjIiwidXNlcl9pZCI6MX0.D4F0iiu6RN2glVtNCWwZf8JuedYBO3dCjjt__oTorWo"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.get(PRODUCT_DETAIL_URL, headers=headers)

if response.status_code == 200:
    product_data = response.json()
    print("Информация о товаре:")
    print(f"ID: {product_data['id']}")
    print(f"Название: {product_data['name']}")
    print(f"Описание: {product_data['description']}")
    print(f"Цена: {product_data['price']}")
    print(f"Категория: {product_data['category']}")
else:
    print(f"Ошибка при получении информации о товаре. Статус код: {response.status_code}")
    print(f"Ответ от сервера: {response.json()}")
