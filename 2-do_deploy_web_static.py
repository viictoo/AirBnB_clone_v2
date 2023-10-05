#!/usr/bin/python3
"""
distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['3.238.28.101', '3.209.82.116']
env.user = 'ubuntu'


# def do_pack():
#     """ fabric script that generates a .tgz """
#     date = datetime.now().strftime("%Y%m%d%H%M%S")
#     path = "versions/web_static_{}.tgz".format(date)
#     try:
#         local("mkdir -p versions")
#         local("tar -czvf {} web_static".format(path))
#         return path
#     except Exception:
#         return None


def do_deploy(archive_path):
    '''use os module to check for valid file path'''
    if os.path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        name = archive.split('.')[0]
        desi = "/data/web_static/releases/{}/".format(name)

        put(archive_path, a_path)
        run("mkdir -p {}".format(desi))
        run("tar -xzf {} -C {}".format(a_path, desi))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(desi, desi))
        run("rm -rf {}web_static".format(desi))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(desi))
        return True
    return False
