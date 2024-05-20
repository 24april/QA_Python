import requests
def checkwebsite(url):
    try:
        if (requests.get(url)).status_code==200:
            return True
        return False
    except:
        return False
url=input("URL:")
print(checkwebsite(url))