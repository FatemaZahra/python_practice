import requests
import json
response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(response.json())
for data in response.json()['abilities']:
    print(data['ability'])

