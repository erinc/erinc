import sys, os
import spotipy
import spotipy.util as util
from firebase import Firebase
f = Firebase('https://erinc.firebaseio.com/blog/', auth_token="novxUZ6B97vTwyPrOWtYGxVFKMgUqQ14cIbR3c3H")

username = "erinc"
scope = 'user-library-read'

SPOTIPY_CLIENT_ID='d121d64f4e5a4f26be72470b6543d732'
SPOTIPY_CLIENT_SECRET='da9a643ed1c44612ab630f0b41206f5a'
SPOTIPY_REDIRECT_URI='http://localhotst/callback'

token = util.prompt_for_user_token(username, scope, client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET, redirect_uri = SPOTIPY_REDIRECT_URI)


if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks(limit=1)
    track = results['items'][0]['track']

    song = track['name'] + ' - ' + track['artists'][0]['name']
    song_link = track['external_urls']['spotify']


    out = '<a target="_blank" href="'+song_link+'">'+song+'</a>'

    f.patch({'song':out})
else:
    print "Can't get token for", username