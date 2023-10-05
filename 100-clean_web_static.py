#!/usr/bin/python3
"""deletes out-of-date archives"""
from fabric.api import *

# env.hosts = ["34.229.70.213", "3.89.160.146"]


@task
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

    try:
        num = int(number)
    except ValueError:
        raise ValueError("Number argument must be a non-negative integer.")

    if num < 0:
        raise ValueError("Number argument must be a non-negative integer.")

    # Local directory clean-up
    local_versions_dir = "versions"
    if num in (0, 1):
        local("cd {} && ls | head -n -1 | xargs rm -rf"
              .format(local_versions_dir))
    elif num >= 2:
        local("cd {} && ls | head -n -{} | xargs rm -rf"
              .format(local_versions_dir, num))

    # Remote directory clean-up
    remote_versions_dir = "/data/web_static/releases"
    try:
        run("cd {} && ls | head -n -{} | xargs rm -rf"
            .format(remote_versions_dir, num))
    except Exception as e:
        print("An error occurred while cleaning remote directory:", e)
