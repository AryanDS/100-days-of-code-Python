import requests
from bs4 import BeautifulSoup

song_date = input("Which year do you want to travel to?, Type the date in this format: YYYY-MM-DD:")
bill_url = "https://www.billboard.com/charts/hot-100/"

URL= f"{bill_url}{song_date}"
CLIENT_ID="02f5b760844d414eb2b9408a361098ef"
CLIENT_SECRET="118436df7b9946fab8c2fe4496b1c888"
REDIRECT_URL="https://developer.spotify.com/dashboard/applications/02f5b760844d414eb2b9408a361098ef"

response  = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())

#Gathering all the song names

# song_names = soup.find_all(name='h3',id= "title-of-a-story")
song_titles = soup.select(selector="li #title-of-a-story")
# print(song_titles)

songs = [i.getText().strip() for i in song_titles]
# print(songs)

##################
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
                                                           client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET ,
                                                           redirect_uri="https://example.com/callback/",
                                                           show_dialog=True,
                                                           cache_path="token.txt"))


user_id = sp.current_user()["id"]

year = song_date.split('-')[0]
song_uris=[]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    #print(type(result))
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)        


playlist = sp.user_playlist_create(user=user_id, name=f"{song_date} Billboard 100", public=False)
# print(playlist)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)