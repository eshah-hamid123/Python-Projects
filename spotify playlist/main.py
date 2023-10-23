from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

year = input('Which year do you want to travel in? ')

url= f'https://digitaldreamdoor.com/pages/bg_hits/bg_hits_{year}.html'
client_id = 'd24d0b8138824f8c91faf669e72e5019'
client_secret = 'b5a32169d94643789970d3dba77c6f59'
redirect_uri = 'http://example.com'

response = requests.get(url)
text = response.text

soup = BeautifulSoup(text, 'html.parser')
song_list = soup.find_all(name='td', class_='s2')
song_names = [song.getText().split('\n')[0] for song in song_list]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope= "playlist-modify-private", show_dialog=True, cache_path="token.txt"))
user_id = sp.current_user()["id"]

all_uri = []

for song in song_names:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        all_uri.append(uri)
    except IndexError:
        print(f'{song} does not exist in Spotify')
all_uri = all_uri[:99]


playlist = sp.user_playlist_create(user_id, f'{year} Top 100 Songs', public=False)

sp.playlist_add_items(playlist_id=playlist['id'], items=all_uri)


