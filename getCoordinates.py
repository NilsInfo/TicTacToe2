import requests

url = 'http://192.168.1.224:8080/qpe/getTagData?tag=a4da22e16f5d'
payload = {}
headers = {}
lastTS = 0
def get():
    response = requests.get(url, headers=headers, data=payload)
    print(response.status_code)

    resJson = response.json()
    return resJson

def getCoordinates():
    resJson = get()
    coordinates = resJson["tags"][0]["locationZoneNames"]
    return coordinates

def getClick():
    global lastTS
    resJson = get()
    print(resJson)
    tS = resJson["tags"][0]["button1LastPressTS"]
    if tS > lastTS:
        lastTS = tS
        return True
    else :
        return False

print(getClick())