#!/usr/bin/python3
""" distributes an archive to your web servers,
    using the function do_deploy
"""
from fabric.api import env, hosts, run, put
from os import path

env.hosts = ['34.229.70.213', '3.89.160.146']


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
        put(archive_path, '/tmp/')

        arch_tgz = archive_path.split('/')[-1]
        arch = arch_tgz.split('.')[0]
        arch_dir = f'/data/web_static/releases/{arch}/'

        run('sudo mkdir -p {}'.format(arch_dir))
        run('sudo tar -xzf /tmp/{} -C {}'.format(arch_tgz, arch_dir))
        run('sudo rm /tmp/{}'.format(arch_tgz))
        run('sudo mv {}web_static/* {}'.format(arch_dir, arch_dir))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(arch_dir))

        print('New version deployed!')
        return True

    except Exception:
        return False
