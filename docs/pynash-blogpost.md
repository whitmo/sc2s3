# Weekend Hacks

## Who & What

Howdy, my name is Whit and I work for SurveyMonkey, who is kind enough to let me work from right here in the Nashdiggity.  I'm one of those programmers who came to talking to the machine through trying to say things on the web. I built my first website in 1996. Just for fun, here's an early site I did both design and programming on: [CHO circa 1997](http://bit.ly/Z1QSwN)).  That fat stack ran perl CGI backed by MSQL (no Y) on AIX. Quicktime vrml and animated gifs were cutting edge back then. 

At that time, hacks were all I knew: photoshop effects, table layouts, duck tape and bailing wire.  Though I've come a long way since, I still appreciate a good hack.  Dirty or elegant, quick or involved, ugly or inspire,  a hack is a heuristic or intuition based implementation that makes what previously was an impediment into a step, a fulcrum, a tool, an anvil, a parachute, an ax to make more hacks.

These days I do most of my hacking in python and I'm honored to be invited to contribute to the pynash blog.  My columns is going to focus on hacks using python as duck tape and super glue. 



## This weeks hack: stream a url into s3

### The problem

Hacking is best when you have something you want to do.  I have a band, and we post our practice sessions to soundcloud.  Soundcloud has a 2hr limit for uploaded music, and well, our band is kinda jammy.  I want to replicate all the recordings into an S3 bucket for safe keeping and hacking ease (say with echonest).

### TL;DR

I'll walk through the process of properly getting started hacking with python IMH&HO. 

We'll use the python http client library [requests](http://docs.python-requests.org) to get data from Soundcloud. We'll talk a bit about the design of what we will do next week using the [AWS python api library](http://aws.amazon.com/sdkforpython/) to concurrently stream files from soundcload to S3.  

### Venv Up! Pip and Paste! Git'r started

No project starts without a sandbox (ie a virtualenv). You may "but it's just a hack", but setting up a proper sandbox is pretty easy. Suave operators use [virtualenv-wrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) so in the interest of being classy, so will we.

This is how I roll when I want to get started (presuming I think it will be more than a gist of code).  After creating a github repo::

```bash
$ cd /to/the/folder/where/the-magic-happens
$ mkvirtualenv sc2s3
(sc2s3)$ pip install pastescript
(sc2s3)$ paster create sc2s3
... answer a bunch of questions about my package
(sc2s3)$ cd ./sc2s3 && wget -O .gitignore http://bit.ly/Z1Tn2e \
             && git init \ 
             && git remote add origin git@github.com:whitmo/sc2s3.git
(sc2s3)$ git add ./ && git commit -m 'gitty up' && git push -u origin master
(sc2s3)$ pip install -e ./
```

The last step puts your new package onto the python path so you start
executing it.

### Technical investigation

We live in the age of P.roggramming B.y G.oogling. Ever watch someone
build a webapp with RoR? In this case, I need to know a bit about
soundcloud and S3.  There is a soundcloud
[actual python library](http://bit.ly/XuMjUU), but I notice that
soundcloud has a fairly rich
[REST/http API](http://developers.soundcloud.com/docs/api/reference#users)
that will give me JSON.  All I need to do is
[set up an application](http://soundcloud.com/you/apps) w/ soundcloud,
and they will give me a client id and an access token.


As all I need is a list of links, I think simply doing some http will
be easiest.  I have a good hammer for this, the
[requests](http://docs.python-requests.org) library by Kenneth
"Kraftwerkzeung" Reitz.

Let's grab it::

```bash
(sc2s3)$ pip install requests
```

Now, lets get prompt.  The python REPL (and it's mutant children like
ipython notebook) rule.  Let's load up our 

```bash
(sc2s3)$ python
>>> import requests
>>> import sc2s3
>>> help(requests)
... # whole lotta on nice documentation
>>> help(sc2s3)
... # whole lotta nada
```

Now we can start to play

```
>>> clid = 'reallysupersecret123'
>>> 
```





## In conclusion

Thanks for reading this far! I'll be blogging every other friday (or saturday).  If you have a fun problem you want to solve using python, twat it to me [@whitmo](https://twitter.com/whitmo) and maybe I'll a crack at it. If you have a great (or awesomely horrible) hack, send me a gist and maybe I'll write about it. If you want to hack with other, contact me or [@firas](https://twitter.com/firas) about Nashdiggity Hacknight(not limited to hacking computers). 
