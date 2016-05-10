import requests
import keys

youtubeurl = "https://www.googleapis.com/youtube/v3"

basicparams = {
    "key":googleapikey,
    "part":"snippet",s
    "q":"google",
}


json = (requests.get(youtubeurl + "/search",  params = basicparams)).json()

print(json["kind"])
