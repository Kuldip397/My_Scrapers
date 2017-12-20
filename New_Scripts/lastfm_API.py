import os
import requests
import shutil


API_key = "02efcda16deea9e8f7f3a6f2b50080c2"
Shared_secret = "d10b99674d9ab3f225d312007f06bbc2"

base_url = " http://ws.audioscrobbler.com/2.0/"

params = {
    "method": "tag.gettopalbums",
    "tag": "pop",
    "api_key": API_key,
    "format": "json",
    "limit": "10",
}

req = requests.get(base_url, params=params)
print(req.status_code)
data = req.json()

albums = data["albums"]["album"]

for album in albums:
    name = album['name']
    artist_name = album['artist']['name']
    image_url = album['image'][3]['#text']
    rank = album['@attr']['rank']
    img_req = requests.get(image_url, stream=True)
    filename = rank + "_" + name + "_" + artist_name + ".png"
    file_path = os.path.join(os.getcwd(), "lastfm_image", filename)
    with open(file_path, "wb") as file:
        shutil.copyfileobj(img_req.raw, file)
    del img_req

