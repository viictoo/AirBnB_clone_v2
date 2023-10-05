#!/usr/bin/python3
"""deletes out-of-date archives
"""
from fabric.api import local, run, env

env.hosts = ['34.229.70.213', '3.89.160.146']


def do_clean(number=0):
    """that deletes out-of-date archives

    Args:
        number (int, optional): number is the number of the archives,
        including the most recent, to keep.
        Defaults to 0.
        If number is 0 or 1, keep only the most recent version of your archive.
        if number is 2, keep the most recent,
        and second most recent versions of your archive
    """

    number = int(number)
    rem = "cd /data/web_static/releases; ls | head -n -{} | xargs rm -rf"
    if number in range(0, 2):
        local("cd versions; ls | head -n -1 | xargs rm -rf")
        run("cd /data/web_static/releases; ls | head -n -1 | xargs rm -rf")
    else:
        local("cd versions; ls | head -n -{} | xargs rm -rf".format(number))
        run(rem.format(number))
