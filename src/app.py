import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
import os
import matplotlib.pyplot as plt

#Spotify Api
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

wknd_uri = "spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spoti = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

wknd_info = spoti.artist(wknd_uri)

top_tracks = spoti.artist_top_tracks(wknd_uri)

print(f'Canciones populares de {wknd_info["name"]}:')

name = []
minutes = []
popularity = []


for track in top_tracks['tracks']:
    name.append(track['name'])
    duracion_en_minutos = round(track['duration_ms']/ 60000, 2)
    minutes.append(duracion_en_minutos)
    popularity.append(track['popularity'])
    print('track     : ' + track['name'])
    print('duration  : ' + str(duracion_en_minutos))
    print('popularity: ' + str(track['popularity']))
    print('----------------------------------')



#Crear dataframe
wknd_ = pd.DataFrame({'Track': name, 'Minutes': minutes, 'popularity': popularity})
wknd_.sort_values(by='popularity',  inplace = True,  ascending=False)
wknd_.head(3)


#Gráfica
plt.figure(figsize=(8, 5))
plt.scatter(wknd_['Minutes'], wknd_['popularity'], alpha=0.5)
plt.title('Relationship between Duration and Popularity of Songs')
plt.xlabel('Minutes')
plt.ylabel('Popularity')
plt.grid(True, color = 'gray', linewidth=0.8)
plt.show()