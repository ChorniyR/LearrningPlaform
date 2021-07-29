import requests


headers = {}
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI3NTU0NDUzLCJqdGkiOiJmMzA1MzdiMmI3Yjk0ZWEwOTVmNGZkYjI2ZTc0YjdjZSIsInVzZXJfaWQiOjJ9._0_YMRooktEYJRttZOINudAy1ty14rGo_Uu_2psjYnM'
headers['Authorization'] = f'Bearer {token} '

r = requests.get(url='http://127.0.0.1:8000/auth/users/me', headers=headers)
print(r.text)
