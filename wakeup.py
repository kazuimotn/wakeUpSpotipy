from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import time

print("明日は何時に起きますか？")
print("HOUR:")
HOUR = int(input())
print("MIN:")
MIN = int(input())

print("何の曲で起きますか？")
print("URI:")
SONG = str(input())

client_credentials_manager = SpotifyClientCredentials("CLIENT ID", "CLIENT SECRET")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = "token"
sp = spotipy.Spotify(auth = token)
while True:
    now = time.localtime()
    if now.tm_hour == HOUR and now.tm_min == MIN:
        sp.start_playback(device_id = "DEVICE ID", context_uri = SONG)
        break
