# https://github.com/spotipy-dev/spotipy/tree/master/examples
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: \n")
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
song_soup = soup.find_all("h3", "a-no-trucate")
song_names = [s.getText(strip=True) for s in song_soup]

# Spotify Authentication
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("CLIENT_ID"),
                                                    client_secret=os.environ.get("CLIENT_SECRET"),
                                                    redirect_uri="http://example.com",
                                                    scope="playlist-modify-private"))

user = spotify.current_user()['id']
name = f"{date} Billboard 100"
print(f"Generating a playlist for user: {user} called {name}")

playlist_id = spotify.user_playlist_create(user, name, public=False, collaborative=False,
                                           description=f'The top 100 songs on {date}')['id']


def get_track_id(song):
    track_id = spotify.search(song, limit=1)['tracks']['items'][0]['uri']
    return track_id


track_ids = [get_track_id(song) for song in song_names]
spotify.playlist_add_items(playlist_id, track_ids)
print("Complete")
