from urllib import response
import requests
import json

ENDPoints = 'https://api.postalpincode.in/pincode/'

pincode = input('Enter Your Pin Code :')
response = requests.get(ENDPoints+pincode)

pincode_info = json.loads(response.text)
print(pincode_info)