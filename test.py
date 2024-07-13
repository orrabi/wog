import requests
from requests.structures import CaseInsensitiveDict

url = "https://openexchangerates.org/api/latest.json?app_id=854fb793dd8f41ab993366ef1ded8390"
resp = requests.get(url)
print(type(resp))
print(resp)
print(resp)
data = resp.json()
rate = data["rates"]["ILS"]
print(type(rate))
print(round(rate,2))