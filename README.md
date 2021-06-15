# Pyke

(WIP, Beta Release) Make-like build automation tool for Python projects with extensive DSL features.

## Features:

+ Users can specify tasks, subtasks, and task rules.
+ Use regex rules patterns to create targets for tasks.
+ Significantly less confusing than Makefiles (is that a <kbd>tab</kbd> or <kbd>space</kbd>...?)
+ Complete Python DSL with full access to builtins and external dependencies.
+ **[WIP]** Run and execute tasks in parallel with each other (threaded multitasking).

## Example:

```python
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
```

Put that in a `Pykefile` and you're good to go. Then run `pyke` in the same directory and watch the magic happen!

```shell
$ pyke dist
Building the project...
Distributing the project...
```

## Installation:

Install the `pykefile` library with `pip`. Requires Python 3.8 or higher.

```shell
python -m pip install pykefile
```

You can also add it your developement dependencies with `poetry`.

```shell
python -m poetry add pykefile --dev 
```

## Usage:

Just like any other Makefile, you'll need the `Pykefile` in your current directory. (`Pykefile.py` also works)

Then use the `pyke` command to execute and run specified tasks. 

Running `pyke` without any commands will call the default task if there is one. The first argument will call a task by that name.

## Developement:

1. Fork the repository: [`Fork`](https://github.com/frissyn/pyke/fork)
2. Clone locally (`git clone https://github.com/<username>/pyke.git`)
3. Create your feature branch (`git checkout -b my-new-feature`)
4. Commit your changes (`git commit -a -m 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a new Pull Request! 🎉

**Local Developement:**

In order to properly test the `pyke` commands, install the package locally like so:

```shell
python -m pip install -e .
```

You can now use `pyke` in your terminal, and it will automatically use the latest changes to the source code. 

Use `bash bin/build` to build the project. `bash bin/docs` will update and start the documentation server locally.

## Final Notes:

Pyke is still in beta and I'm open to feature requests or bug reports. Feel free to open an issue! Thanks for checking this project out and I hope it'll make your Python developement process easier!
