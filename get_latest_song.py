import sys, os
import spotipy
import spotipy.util as util

script_dir = os.path.dirname(__file__)
song_file_path = os.path.join(script_dir, 'templates/_song.txt')

token = "BQDwFWLUgNOwgkesvK_ek3KPHhzaZeFas9HTgrWEr6LmYPzz3hUwXOJ73XNw-MziQoQs6MI2S6qzQxFNN1Mnl00-Y8LsHh9X4Q0tgK1xkVjKGqgc1vz-94y6eKcUm3oibdo_jkKvtq6-sL57qkcMiA"

sp = spotipy.Spotify(auth=token)
results = sp.current_user_saved_tracks(limit=1)
track = results['items'][0]['track']

song = track['name'] + ' - ' + track['artists'][0]['name']
song_link = track['external_urls']['spotify']


out = '<a target="_blank" href="'+song_link+'">'+song+'</a>'

with open(song_file_path, 'w') as the_file:
    the_file.write(out)
