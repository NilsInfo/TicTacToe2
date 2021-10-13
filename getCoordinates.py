import requests

url = 'http://192.168.1.224:8080/qpe/getTagData'
options = "?mode=json&tag='a4da22e16f5d"
req = url + options
payload = {}
headers = {}


def getCoordinates():

    response = requests.get(url, headers=headers, data=payload)
    resJson = response.json()
    print(response.status_code)
    coordinates = resJson["tags"][0]["location"]
    return {coordinates[0],coordinates[1]}

print(getCoordinates())