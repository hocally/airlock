import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

for track in get_playlist_tracks('daliberator', '0N6PJagAmb20ioTGX7DtZF'):
    print(track['track']['name'])