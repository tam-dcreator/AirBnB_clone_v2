#!/usr/bin/python3
import os
from fabric.api import *
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
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
