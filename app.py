from cnf import CLIENT_ID, CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta

scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=scope
))

def extract(date, limit=50):
    ds = int(date.timestamp()) * 1000
    return sp.current_user_recently_played(limit=limit, after=ds)


