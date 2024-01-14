#!/usr/bin/python3
from datetime import datetime
from fabric.api import local
"""function do_pack"""


def do_pack():
    """
    script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo
    """
    current = datetime.now()
    name = "web_static_{}{}{}{}{}{}.tgz".format(current.year, current.month, current.day, current.hour, current.minute, current.second)
    cmd = local("tar -cvf %s /web-static -C /versions" % (name))
    if cmd.succeeded:
        return 
    else:
        return None
