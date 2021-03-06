import sys as _sys

from conda_cookie.cookie import Cookie, create_project_skeleton


def cut_project(name, path, conf=None):
    cookie = Cookie(name, path, conf=conf)
    create_project_skeleton(cookie)
    cookie.initial_commit()
    cookie.create_conda_env()
    cookie.develop_install()
    cookie.push_to_github()
