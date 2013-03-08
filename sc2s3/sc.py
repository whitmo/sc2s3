import requests
import json

class SoundcloudAPIError(RuntimeError):
    """
    SC is broke
    """

def track_data(client_id, username):
    url = 'http://api.soundcloud.com/users/{username}/tracks.json?client_id={client_id}'.format(**locals())
    res = requests.get(url)
    if res.status_code == 200:
        tracks = json.loads(res.content)
        return tracks
    raise SoundcloudAPIError("{}{}:{}".format(res.status_code, res.reason, res.content))


def downloadable(trax):
    for track in trax:
        if 'downloadable' in track:
            yield track['download_url'], track


def list_urls(client_id, username):
    trax = track_data(client_id, username)
    return (('title', 'url', 'date', 'description'), 
            ((data['title'], url, data['created_at'], data['description']) for url, data in downloadable(trax)))

