## code to capture currency conversion rate and write to text file

import requests
import json

url = "https://exchange-rate-api1.p.rapidapi.com/convert"

# change base and target values with corresponding currency codes 
querystring = {"base":"USD","target":"KRW"}

# insert user's API key value to test 
headers = {
	"X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
	"X-RapidAPI-Host": "exchange-rate-api1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

# take JSON response and write to text file every time request is made
with open("conversion.txt", "a") as f:
    json.dump(response.json(), f, indent=2)
f.close()
