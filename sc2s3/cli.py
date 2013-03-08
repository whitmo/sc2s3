from .sc import list_urls
from cStringIO import StringIO as strio
from cliff.app import App
from cliff.commandmanager import CommandManager
from cliff.lister import Lister
from itertools import count
import logging
import pkg_resources
import requests
import sys
import urllib


class CLIApp(App):
    """
    command line interface
    """
    specifier = 'sc2s3.cli'
    version = pkg_resources.get_distribution('sc2s3').version
    log = logging.getLogger(__name__)

    def __init__(self):
        super(CLIApp, self)\
            .__init__(description=self.specifier,
                      version=self.version,
                      command_manager=CommandManager(self.specifier))


class SCUrls(Lister):
    list_urls = staticmethod(list_urls)
    def get_parser(self, prog_name):o
        parser = super(SCUrls, self).get_parser(prog_name)
        parser.add_argument('clientid', 
                            help="Sound cloud client id")
        parser.add_argument('username', 
                            help="Sound cloud username")
        return parser

    def take_action(self, pargs):
        """
        enqueue a job
        """
        return self.list_urls(pargs.clientid, pargs.username)

        
def main(argv=sys.argv[1:], app=CLIApp):
    return app().run(argv)


logger = logging.getLogger(__name__)

#ced262b670362c8fc4d307f0d20a3d48







def make_key(track_md):
    title = track_md['title']
    id_ = track_md['id']
    return "{}-{}".format(id_, urllib.quote(title))


def download_upload(url, key, bucket, extra={}, redundancy=True):
    res = requests.get(url, stream=True)
    mp = bucket.initiate_multipart_upload(key, metadata=extra, reduced_redundancy=not redundancy)
    idx = count()
    for block in res.iter_content:
        mp.upload_part_from_file(strio(block), next(idx))


def stream_to_s3():
    url = "http://%s.s3.amazonaws.com/%s" % (bucket, filename)



#https://gist.github.com/mattbillenstein/1471499
#http://blog.odonnell.nu/posts/streaming-uploads-s3-python-and-poster/
#concurrent downloader


