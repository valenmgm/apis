import requests

paramters = {
    "ts":1,
    "apikey":"6b2b4e4dad645c82c15769043f414a81",
    "hash":"f58e572eaa92e2adb3108bd919285ac9",
}

resultado = ""

def getCharacter():
    fulllist = (requests.get("http://gateway.marvel.com:80/v1/public/characters", params=paramters)).json()

    for character in fulllist["data"]["results"]:
        print(character["name"])
        print(character["id"])
 #   for element in characters:
  #      print(element["name"])

getCharacter()

def characterStories():
    stories = (requests.get("http://gateway.marvel.com:80/v1/public/characters/1011031/stories", params=paramters)).json()
    for element in stories["data"]["results"]:
        print(element["title"])

characterStories()