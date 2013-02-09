import grequests
import json
import logging
import requests
import urlparse
from cStringIO import StringIO as strio

logger = logging.getLogger(__name__)


def track_data(client_id, username):
    url = 'http://api.soundcloud.com/users/{username}/tracks.json?client_id={id}'.format(**locals())
    res = requests.get(url)
    if res.status_code == 200:
        tracks = json.load(res.content)
        return tracks, True
    return None, res


def trax2urls(trax):
    for track in trax:
        if 'downloadable' in track:
           yield track['download_url']



def download_upload(url, bucket, redundancy=True):
    res = requests.get(url, stream=True)
    mp = bucket.initiate_multipart_upload(fpath, reduced_redundancy=not redundancy)
    for block in res.iter_content:

        pass


def stream_to_s3():
    url = "http://%s.s3.amazonaws.com/%s" % (bucket, filename)



#https://gist.github.com/mattbillenstein/1471499
#http://blog.odonnell.nu/posts/streaming-uploads-s3-python-and-poster/
#concurrent downloader
