import requests
import json


out = json.loads(requests.get("https://fakestoreapi.com/products").text)



print(out[2]["title"])


