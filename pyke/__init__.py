"""
Pyke: Makelike build tool for Python
~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+~=+
"""

import typing as t

__title__       = "pyke"
__author__      = "frissyn"
__version__     = "0.0.4"
__license__     = "MIT"
__package__     = "pyke"
__description__ = "Makelike build tool for Python."

tasks: t.Mapping = {}

from .task import task
from .task import get_task
from .task import exec_task
from .task import default_task

from .core import env
from .core import run
from .core import shell
from .core import export

from .runner import runner