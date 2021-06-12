import os
import sys
import platform
import typing as t
import subprocess as sp

from pyke import tasks
from pyke import exec_task
from pyke import errors as e


def env(key: t.Text, default: t.Optional[t.Any] = None) -> t.Any:
    return os.environ.get(key, default)


def export(**kv: t.Any) -> t.Union[t.Any, t.NoReturn]:
    cmd = "export"

    if platform.system() == "Windows":
        cmd = "set"
    
    for k, v in kv.items():
        os.environ[k] = str(v)
        sp.Popen(f"{cmd} {k}={v}", stdout=sp.PIPE, shell=True)

    if len(kv.keys()) == 1:
        return list(kv.values())[0]
    else:
        return


def run() -> t.NoReturn:
    args = []

    for i, value in enumerate(sys.argv):
        if value == "---":
            args = sys.argv[i + 2 :]

    if args == list(["--help"]):
        print(__import__("pyke").__doc__)
        exit(0)

    if not args:
        todo = [t for n, t in tasks.items() if t["o"].get("default")]

        if not todo:
            raise e.NoDefaultTaskError
        else:
            exec_task(todo[0])
            exit(0)
    else:
        exec_task(args[0])
        exit(0)


def shell(cmd: t.Text) -> sp.CompletedProcess:
    return sp.run(cmd, shell=True)
