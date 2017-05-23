import argparse
import sys
import conda_cookie.api as api
from attrdict import AttrDict


def parse_args(args):
    p = argparse.ArgumentParser()
    p.description = """
Tool for initializing a new python project. It takes care of setting up git, github, travisci,
versioning, setup.py, and more."""
    subparsers = p.add_subparsers(dest="command")
    cut_p = subparsers.add_parser("cut")
    cut_p.add_argument('name', metavar='PROJECT_NAME',
                       help='name of project')
    cut_p.add_argument('path', metavar='PROJECT_PATH',
                       help='path where the project will be created')
    cut_p.add_argument('--python', metavar='PYTHON_VER', default='3.6',
                       help='Set the Python version used by conda.')
    cut_p.add_argument('--github-ssh', action='store_true', default=False,
                       help='Use ssh with Github.')
    args = p.parse_args(args)
    return p, args


def execute(args):
    parser, args = parse_args(args)
    config = AttrDict(args.__dict__)
    if args.command == 'cut':
        api.cut_project(config.name, config.path, config)
    else:
        parser.print_help()
        raise ValueError("Unknown command: {}".format(args.command))


def main():
    execute(sys.argv[1:])


if __name__ == '__main__':
    main()
