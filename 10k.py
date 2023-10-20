#!/usr/bin/python3
"""
distributes an archive to your web servers,
using the function do_deploy
fab -f 3-deploy_web_static.py deploy -i my_ssh_private_key -u ubuntu
"""
from fabric.api import env, run, put, task
from datetime import datetime
import os

env.hosts = ["34.229.70.213", "3.89.160.146"]


@task
def do_deploy(archive_path):

    try:

        arch_tgz = archive_path.split("/")[-1]
        arch = arch_tgz.split(".")[0]
        # arch_dir = "/data/web_static/releases/{}/".format(arch)
        arch_dir = '/data/web_static/releases/' + arch + '/'
        no_ext = archive_path.split("/")[-1]
        #     without = no_ext.split(".")[0]
        #     # fn_no_ext = os.path.splitext(fn_with_ext)[0]
        #     dpath = '/data/web_static/releases/' + without + '/'

        #     # put(archive_path, "/tmp/")
        # put(archive_path, "/tmp/")

        #     print("New version deployed!")
        #     return True

        # except Exception:
        #     return False



        no_ext = archive_path.split("/")[-1]
        without = no_ext.split(".")[0]
        # fn_no_ext = os.path.splitext(fn_with_ext)[0]
        dpath = '/data/web_static/releases/' + without + '/'

        put(archive_path, "/tmp/")
    except Exception:
        return False


    # put(archive_path, "/tmp/")
    # run("rm -rf {}{}/".format(dpath, fn_no_ext))
    # run("mkdir -p {}{}/".format(dpath, fn_no_ext))
    # run("tar -xzf /tmp/{} -C {}{}/".format(fn_with_ext, dpath, fn_no_ext))
    # run("rm /tmp/{}".format(fn_with_ext))
    # run("mv {0}{1}/web_static/* {0}{1}/".format(dpath, fn_no_ext))
    # run("rm -rf {}{}/web_static".format(dpath, fn_no_ext))
    # run("rm -rf /data/web_static/current")
    # run("ln -s {}{}/ /data/web_static/current".format(dpath, fn_no_ext))
    print("New version deployed!")

