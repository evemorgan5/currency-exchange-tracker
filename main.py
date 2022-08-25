# @@@@@@@@ Virtual Environment should be used whenever you work on any Python based project.
# FIXME: set up virtual env

# first step need to get data from currency api


#  currency exchange info
#  https://apilayer.com/marketplace/order_complete?id=223&txn=free&e=Sign%20Up&l=Success


# make request to api to get data

# need to pip3 install requests
import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=USD&from=EUR&amount=1"

payload = {}
headers= {
  "apikey": "q7LWYZVEKHqJ2lckkzUdvIfgzyIiisL8"
}


response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text