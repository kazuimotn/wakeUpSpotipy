from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import time
from PIL import Image

print("明日は何時に起きますか？")
print("HOUR:")
HOUR = int(input())
print("MIN:")
MIN = int(input())

print("何の曲で起きますか？")
print("URI:")
SONG = str(input())

im = Image.open("white.png")

client_credentials_manager = SpotifyClientCredentials("b271a0e85639470a95195eb71135ad98", "dde1d4b16992450e86b5490eef652fc9")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = "BQDOT7uxLwiYyRGaLM1fmE2dYEJazvHYv6B5SixV1J69PbLZvwZ1rjqBxLBos5hpPxkRU5mlYr1YNJqrpxtgluRQPlU-Y2YHpVSd31dOh0Cj51ohpCPoB_ZV-Y9W9DM_eD69lhwhBRHxhIITNabMFQBkJ8mQnSBlKPQ6NMf-PeVHFEtKS2gynsW5vKKd5FmEQ9NbwxNFh5SJo5fKrtFKraLteWHGRNoHmP6tNBNB49mkF8HLRdL6uXkBlenxL3BlWfXNbpVTTg7os_O-SaYxbQw1W51TsPh0FXX2-hM"
sp = spotipy.Spotify(auth = token)
while True:
    now = time.localtime()
    if now.tm_hour == HOUR and now.tm_min == MIN:
        sp.start_playback(device_id = "fa8953033913a092cc25ec415f768d02bfb5d469", context_uri = SONG)
        im.show()
