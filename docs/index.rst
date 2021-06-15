.. pyke documentation master file, created by
   sphinx-quickstart on Tue Jun 15 00:29:07 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pyke - Make for Python
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api


(WIP, Beta Release) Makelike build automation tool for Python projects
with extensive DSL features. Throwout your Makefiles and use Pykefiles!

Features
--------

1. Users can specify tasks, subtasks, and task rules.
2. Use regex rules patterns to create targets for tasks.
3. Significantly less confusing than Makefiles (is that a tab or
   space...?)
4. Complete Python DSL with full access to builtins and external
   dependencies.
5. **[WIP]** Run and execute tasks in parallel with each other (threaded
   multitasking).

Example
-------

.. code:: python

   import pyke

   # create a defualt task, named "build"
   @pyke.task("build", default=True)
   def build():
       print("Building the project...")

   # create a task dependency. running `pyke dist` 
   # will make the "build" task run first! 
   @pyke.task("dist", deps=["build"])
   def dist():
       print("Distributing the project...")

   pyke.run()

Put that in a ``Pykefile`` and you're good to go. Then run ``pyke`` in
the same directory and watch the magic happen!

.. code:: shell

   $ pyke dist
   Building the project...
   Distributing the project...

Installation
------------

Install the ``pykefile`` library with ``pip``. Requires Python 3.8 or
higher.

.. code:: shell

   python -m pip install pykefile

You can also add it your developement dependencies with ``poetry``.

.. code:: shell

   python -m poetry add pykefile --dev 

Usage
-----

Just like any other Makefile, you'll need the ``Pykefile`` in your
current directory. (``Pykefile.py`` also works)
Then use the ``pyke`` command to execute and run specified tasks.
Running ``pyke`` without any commands will call the default task if
there is one. The first argument will call a task by that name.