# Pyke

(WIP, Beta Release) Make-like build automation tool for Python projects with extensive DSL features.

### Features:

+ Users can specify tasks, subtasks, and task rules.
+ Significantly less confusing than Makefiles (is that a <kbd>tab</kbd> or <kbd>space</kbd>...?)
+ Complete Python DSL with full access to builtins and external dependencies.
+ Run and execute tasks in parallel (multitasking) (task is a recurring theme, huh...).

### **Example:**

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

### Installation:

Install the `pykefile` library with `pip`. Requires Python 3.8 or higher.

```shell
python -m pip install pykefile
```

You can also add it your developement dependencies with `poetry`.

```shell
python -m poetry add pykefile --dev 
```

### Usage:

Just like any other Makefile, you'll need the `Pykefile` in your current directory. (`Pykefile.py` also works)

Then use the `pyke` command to execute and run specified tasks. 

Running `pyke` without any commands will call the default task if there is one. The first argument will be call a task by that name.


### Final Notes:

Pyke is still in beta and I'm open to feature requests or bug reports. Feel free to open an issue! Thanks for checking this project out and I hope it'll make your Python developement process easier!