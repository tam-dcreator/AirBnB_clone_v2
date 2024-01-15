#!/usr/bin/python3
import os
from fabric.api import env
env.hosts = ['100.25.151.158', '34.207.57.64']
"""
Fabric script (based on the file 3-deploy_web_static.py) that
deletes out-of-date archives, using the function do_clean
"""


def do_clean(number=0):
    """
    number is the number of the archives, including the most recent, to keep.
        If number is 0 or 1, keep only the most recent version of your archive.
        if number is 2, keep the most recent,
        and second most recent versions of your archive.
    Your script should:
        Delete all unnecessary archives
        (all archives minus the number to keep) in the versions folder
        Delete all unnecessary archives
        (all archives minus the number to keep) in the
        /data/web_static/releases folder of both of your web servers
    """
    files = os.listdir('/versions').sort()
    for f in files:
        if 'web_static' not in f or '.tgz' not in f:
            files.remove(f)
    if number >= 0:
        if number in (0, 1):
            for i in range(len(files) - 1):
                run("rm -rf /versions/{}".format(files[i]))
        else:
            for i in range(len(files) - number):
                run("rm -rf /versions/{}".format(files[i]))
