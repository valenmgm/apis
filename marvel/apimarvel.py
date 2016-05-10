import requests
import keys


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
