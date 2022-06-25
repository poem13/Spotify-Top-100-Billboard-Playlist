import argparse
from pprint import pprint
import requests
import spotify
import spotipy
from spotipy import SpotifyOAuth
from bs4 import BeautifulSoup

OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="6ac27e6883074ddd8883f3f47f66ad71",
        client_secret="32259d62847c453c8669edb4878e3bd6",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")
song_titles = [song.getText().strip("\t\t\n\t\n") for song in titles]
year = date.split("-")[0]
print(song_titles)

song_uris = []
for i in song_titles:
    result = sp.search(q=f"track:{i}, year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{i} does not exist in Spotify. Skipping...")
print(song_uris)

playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False)
playlist_id = playlist["id"]
print(playlist_id)
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
