## code to capture currency conversion rate and write to text file

import requests
import json

url = "https://exchange-rate-api1.p.rapidapi.com/convert"

# change base and target values with corresponding currency codes 
querystring = {"base":"USD","target":"MXN"}

# insert user's API key value to test 
headers = {
	"X-RapidAPI-Key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
	"X-RapidAPI-Host": "exchange-rate-api1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring).json()

# capture values for rate, base, and target in json response
rate = str(response["convert_result"]["rate"])
base = response["convert_result"]["base"]
target = response["convert_result"]["target"]

# write conversion rate in readable format
f = open("conversion.txt", "a")
f.write("The conversion rate for " + base + " to " + target + " is " + rate + ".\n\n")    
f.close()
