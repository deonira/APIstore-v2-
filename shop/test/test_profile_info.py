import requests

user_profile_url = 'http://127.0.0.1:8000/store/api/user-profile/'

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODc3ODAzLCJpYXQiOjE3MjU4Nzc1MDMsImp0aSI6ImU5YWU3YmNmYmFhYTQ0NGY4ODc5NmJlNDYxOTUyNGQ2IiwidXNlcl9pZCI6MX0.4Cu_akmEgaLT708Hu-vDdfh_WO_z6xWu48M0kWpPuA8"

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.get(user_profile_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    user_data = data.get('user', {})
    profile_data = data.get('profile', {})

    print("User Information:")
    print(f"Username: {user_data.get('username')}")
    print(f"Email: {user_data.get('email')}")

    print("\nProfile Information:")
    print(f"Address: {profile_data.get('address')}")
    print(f"Phone Number: {profile_data.get('phone_number')}")
else:
    print(f"Error fetching user profile. Status code: {response.status_code}")
    print(f"Response: {response.text}")
