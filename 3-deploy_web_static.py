#!/usr/bin/python3
from fabric.api import env
pack = __import__('1-pack_web_static').do_pack
dep = __import__('2-do_deploy_web_static')
env.hosts = ['100.25.151.158', '34.207.57.64']
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy
"""


def deploy():
    """
    The script should take the following steps:
        Call the do_pack() function and store
        the path of the created archive
        Return False if no archive has been created
        Call the do_deploy(archive_path) function,
        using the new path of the new archive
        Return the return value of do_deploy
    """
    archive = pack()
    if archive is False:
        return False
    return dep.do_deploy(archive)
