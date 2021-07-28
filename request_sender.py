import requests


headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI3NDc2NTA0LCJqdGkiOiIyYjMyMzM4YWM3Zjg0ZDUzYTdmZDhlZDY0Mzc4MWVjZCIsInVzZXJfaWQiOjF9.fc0Nlk_Pr0mZB6iBoVOFRJfaR1uGKx0R7eXAzeJbmdE'

r = requests.get(url='http://127.0.0.1:8000/courses/1', headers=headers)
print(r.text)
