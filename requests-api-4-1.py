import requests

response = requests.get('https://api.github.com')

print(response.status_code)

print(response.reason)

print(response.headers)

print(response.url)

print(response.history)

response = requests.get('http://api.github.com')
response.history

response = requests.get('https://api.github.com')
response.elapsed
response.request
response.request.headers

response.encoding
response.content
response.text
response.json()
response.json()['team_url']