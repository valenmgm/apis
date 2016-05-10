import requests

apikey = "AIzaSyCwTBG3eNDtVVWal-HbfqLyxpvdhg7N_Rk"
youtubeurl = "https://www.googleapis.com/youtube/v3"

basicparams = {
    "key":apikey,
    "part":"snippet",
    "q":"google",
}


json = (requests.get(youtubeurl + "/search",  params = basicparams)).json()

print(json["kind"])
