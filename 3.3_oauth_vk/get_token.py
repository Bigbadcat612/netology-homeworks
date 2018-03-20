import requests
from urllib.parse import urlencode

APP_ID = 6413759
AUTH_URL = 'https://oauth.vk.com/authorize'

auth_data = {
    'client_id': 6413986,
    'display': 'popup',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.73',
    'revoke': 1
}

def get_oauth_url():
    oauth_url = '?'.join((AUTH_URL, urlencode(auth_data)))
    return oauth_url
    
print(get_oauth_url())