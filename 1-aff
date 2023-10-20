#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from
    the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    All files in the folder web_static must be added to the final archive
    All archives must be stored in the folder versions
    (function should create this folder if it doesn’t exist)
    The name of the archive created must be
    web_static_<year><month><day><hour><minute><second>.tgz
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    arch_name = "web_static_{}.tgz".format(date)
    try:
        local('mkdir -p versions')
        local('tar -cvzf versions/{} web_static'.format(arch_name))
        return "versions/{}".format(arch_name)
    except Exception:
        return None
