import sys as _sys

# make the Config class available in the api namespace
from conda_cookie.cookie import Cookie, create_project_skeleton


def cut_project(name, path, conf=None):
    cookie = Cookie(name, path, conf=conf)
    create_project_skeleton(cookie)
    cookie.initial_commit()
    python_ver = input("Enter python version [2.7]: ") or '2.7'
    cookie.create_conda_env(python_ver)
    cookie.develop_install()
    cookie.push_to_github()
