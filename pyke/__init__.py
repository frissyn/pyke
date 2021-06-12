"""
Pyke: Makelike build tool for Python
~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+
"""

import typing as t

__title__       = "pyke"
__author__      = "frissyn"
__version__     = "0.0.1a"
__license__     = "MIT"
__package__     = "pyke"
__description__ = "Make-like build tool for Python."

tasks: t.Mapping = {}

from .task import task
from .task import exec_task

from .core import run
from .core import runner