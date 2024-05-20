import requests


resp = requests.get('https://ya.ru')
print(resp.text)