import requests

response = requests.delete("http://127.0.0.1:3000/api/courses/1")
print(response.json())
