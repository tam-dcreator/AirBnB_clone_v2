#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy
"""


def do_deploy(archive_path):
    """
    Returns False if the file at the path archive_path doesn’t exist
    The script should take the following steps:
        Upload the archive to the /tmp/ directory of the web server
        Uncompress the archive to the folder
        /data/web_static/releases/<archive filename without extension>
        on the web server
        Delete the archive from the web server
        Delete the symbolic link /data/web_static/current from the web server
        Create a new the symbolic link /data/web_static/current
        on the web server, linked to the new version of your code
        (/data/web_static/releases/<archive filename without extension>)
    """
    pass
