import requests

try:
    site = requests.get("http://pudim.com.br/")
    print("Site no ar!")
except Exception as e:
    print("Site fora do ar!")
