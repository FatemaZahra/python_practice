import requests
import json
# response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
#
# print(response.json())
# for data in response.json()['abilities']:
#     print(data['ability'])

#Verify postcode entered by user is valid or invalid

user_input = input("Please enter your Postcode")

postcode_response = requests.get(f"https://api.postcodes.io/postcodes/{user_input}")
# print(postcode_response.json()) --> to check if the response is working

if postcode_response.json()['status'] == 200:
    print("Valid postcode")
else:
    print("Invalid postcode")


