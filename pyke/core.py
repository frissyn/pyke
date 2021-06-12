import os
import sys
import typing as t

from pyke import tasks
from pyke import exec_task
from pyke import errors as e

def run() -> t.NoReturn:
    args = []

    for i, value in enumerate(sys.argv):
        if value == "---":
            args = sys.argv[i + 2:]

    if args == list(["--help"]):
        print(__import__("pyke").__doc__); exit(0)
    
    if not args:
        todo = [t for n, t in tasks.items() if t["o"].get("default")]

        if not todo:
            raise e.NoDefaultTaskError
        else:
            exec_task(todo[0]); exit(0)
    else:
        exec_task(args[0]); exit(0)


def runner() -> t.NoReturn:
    argstr = ' '.join(sys.argv)
    cmd = "python Pykefile"

    code = os.system(f"{cmd} --- {argstr}")

    exit(code)