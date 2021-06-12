import typing as t

from pyke import tasks
from pyke import errors as e


def task(*args, **options: t.Any) -> t.Callable:
    def decorator(func: t.Callable) -> t.Callable:
        try:
            name = args[0]
        except IndexError:
            name = func.__name__

        tasks[name] = {"f": func, "o": options}

        return func

    return decorator


def exec_task(task: t.Union[t.Mapping, t.Text]) -> t.Any:
    if isinstance(task, t.Text):
        task: t.Mapping = tasks[task]

    opts = task["o"]

    if opts.get("deps"):
        for i in opts["deps"]:
            try:
                tasks[i]["f"]()
            except KeyError:
                raise e.NoTaskFoundError(i)

    return task["f"]()
