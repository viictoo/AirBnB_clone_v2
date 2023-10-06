#!/usr/bin/python3
"""deletes out-of-date archives"""
from os import path
from datetime import datetime
from fabric.api import local, run, task, env, runs_once
env.hosts = ["34.229.70.213", "3.89.160.146"]


@runs_once
def do_clean_local(num):
    local_versions_dir = "versions"
    if num in (0, 1):
        local("cd {} && ls -t | head -n -1 | sudo xargs rm -rf"
              .format(local_versions_dir))
    elif num >= 2:
        local("cd {} && ls -t | head -n -{} | sudo xargs rm -rf"
              .format(local_versions_dir, num))


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
        return False

    if num < 0:
        return False

    # Local directory clean-up
    do_clean_local(num)
    # Remote directory clean-up
    remote_versions_dir = "/data/web_static/releases"
    if num in (0, 1):
        run("cd {} && ls -t | head -n -1 | sudo xargs rm -rf"
            .format(remote_versions_dir))
    elif num >= 2:
        run("cd {} && ls -t | head -n -{} | sudo xargs rm -rf"
            .format(remote_versions_dir, num))

    # try:
    #     run("cd {} && ls -t | head -n -{} | sudo xargs rm -rf"
    #         .format(remote_versions_dir, num))
    # except Exception:
    #     pass
