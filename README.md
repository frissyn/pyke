# Pyke

Make-like build automation tool for Python projects with extensive DSL features.

**Features:**

+ Complete Python DSL with full access to builtins and external dependencies.
+ Users can specify tasks, subtasks, and task rules.
+ Run and execute tasks in parallel (multitasking) (task is a recurring theme, huh...).

**Example:**

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
```

Put that in a `Pykefile` and you're good to go. Then run `pyke` in the same directory and watch the magic happen!

```shell
$ pyke dist
Building the project...
Distributing the project...
```
