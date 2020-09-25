import requests

url = "https://api.chucknorris.io/jokes/random"

payload = {}
headers = {
  'Cookie': '__cfduid=d2dc6733d0088609091186ea5d0fe4a001600287049'
}

response = requests.request("GET", url, headers=headers, data = payload)

jsonresponse = response.json()

print(response.text.encode('utf8'))
print()

print("The Chuck Norris Joke is:")
print(jsonresponse['value'])
