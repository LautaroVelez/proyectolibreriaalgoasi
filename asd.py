import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

username = '11132663303'
client_id ='745fd417f4624477bbd3b7483a6085eb'
client_secret = 'bcfb8eef7da34c1d9353d3d63aa9fd5e'
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-recently-played'

token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)