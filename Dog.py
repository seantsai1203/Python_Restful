import requests #載入requests模組
import json #載入json模組, 原本是json,要轉化成python可以讀的格式

url = "https://dog.ceo/api/breeds/image/random"

payload = {}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

data=json.loads(response.text) #json格式資料,要去讀取response.text, 轉換成data
print(data['message'])
