#!/usr/bin/python3
from datetime import datetime
from fabric.api import local
import os
"""function do_pack"""


def do_pack():
    """
    script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo
    """
    current = datetime.now()
    name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            current.year, current.month, current.day,
            current.hour, current.minute, current.second)
    if not os.path.exists('versions'):
        os.mkdir('versions')
    if local("tar -cvzf %s web_static" % (name)).succeeded:
        return name
    else:
        return None
