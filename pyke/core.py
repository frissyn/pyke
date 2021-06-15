import os
import sys
import platform

import typing as t
import subprocess as sp

from pyke import get_task
from pyke import exec_task
from pyke import default_task
from pyke import errors as e

from pyke import __doc__ as dcs


def env(key: t.Text, default: t.Optional[t.Any] = None) -> t.Any:
    """
    Wrapper function for ``os.environ.get`` to access enviornment
    variables in your tasks.
    
    :param key: Dictionary key to get.
    :type key: ``Text``
    :param default: Value to return if key isn't found. Defaults to ``None``.
    :type default: ``Any``, optional

    :rtype: ``Any``
    """
    return os.environ.get(key, default)


def export(**kv: t.Any) -> t.Union[t.Any, t.NoReturn]:
    """
    Sets given mapping of keyword arguments as enviornment
    variables that can be accessed from ``pyke.env`` or 
    ``os.environ``. Uses OS independent method to set env 
    vars in running process.

    :rtype: ``Union[Any, NoReturn]``
    """

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
    """
    Starts the Pykefile runner and parses ``sys.argv`` to run specified
    tasks. Should only be run `after` all tasks have been specified.

    :rtype: ``NoReturn``
    """
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
    """
    Wrapper function for ``subprocess.run``. Runs given
    command in the shell and returns the completed process.

    :param cmd: Command to run in the shell.
    :type cmd: ``Text``

    :rtype: ``subprocess.CompletedProcess``
    """
    return sp.run(cmd, shell=True)
