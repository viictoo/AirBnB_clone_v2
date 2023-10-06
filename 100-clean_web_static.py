#!/usr/bin/python3
"""deletes out-of-date archives"""
from fabric.api import *
from os import path
from datetime import datetime
from fabric.api import local
env.hosts = ["34.229.70.213", "3.89.160.146"]


@runs_once
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


@task
def do_deploy(archive_path):
    """
    Upload the archive to the /tmp/ directory of the web server
    Uncompress the archive to the folder
    /data/web_static/releases/<archive filename without extension>
    on the web server
    Delete the archive from the web server
    Delete the symbolic link /data/web_static/current from the web server
    Create a new the symbolic link /data/web_static/current on the web server,
    linked to the new version of the code
    /data/web_static/releases/<archive filename without extension>
    True if all operations have been done correctly, otherwise returns False
    """
    if not path.exists(archive_path):
        return False
    try:

        arch_tgz = archive_path.split('/')[-1]
        arch = arch_tgz.split('.')[0]
        arch_dir = '/data/web_static/releases/{}/'.format(arch)

        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(arch_dir))
        run('tar -xzf /tmp/{} -C {}'.format(arch_tgz, arch_dir))
        run('rm /tmp/{}'.format(arch_tgz))
        run('sudo mv {}web_static/* {}'.format(arch_dir, arch_dir))
        run('rm -rf {}web_static'.format(arch_dir))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(arch_dir))

        print('New version deployed!')
        return True

    except Exception as e:
        print(e)
        return False


@task
@runs_once
def deploy():
    """
    Call the do_pack() function and store the path of the created archive
    Return False if no archive has been created
    Call the do_deploy(archive_path) function, using the new
    path of the new archive
    Return the return value of do_deploy
    """
    try:
        archive_path = do_pack()
        if archive_path is None:
            return False
        ret = do_deploy(archive_path)
        return ret
    except Exception:
        return False


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
    local_versions_dir = "versions"
    if num in (0, 1):
        local("cd {} && ls -t | head -n -1 | sudo xargs rm -rf"
              .format(local_versions_dir))
    elif num >= 2:
        local("cd {} && ls -t | head -n -{} | sudo xargs rm -rf"
              .format(local_versions_dir, num))

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
