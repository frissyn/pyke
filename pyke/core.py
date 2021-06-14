import os
import re
import sys
import platform

import typing as t
import subprocess as sp

from pyke import tasks
from pyke import get_task
from pyke import exec_task
from pyke import default_task
from pyke import errors as e

from pyke import __doc__ as dcs


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
        print(dcs)
        exit(0)

    if not args:
        todo = default_task()

        if not todo:
            raise e.NoDefaultTaskError
        else:
            exec_task(todo, args[0:])
    else:
        task = get_task(' '.join(args))

        if not task:
            raise e.NoTaskFoundError()

        exec_task(task, args)
    
    exit(0)


def shell(cmd: t.Text) -> sp.CompletedProcess:
    return sp.run(cmd, shell=True)
