import re

import typing as t

from pyke import tasks
from pyke import errors as e


def task(*args, **options: t.Any) -> t.Callable:
    def decorator(func: t.Callable) -> t.Callable:
        try:
            name = args[0]
        except IndexError:
            if options.get("pattern"):
                name = options["pattern"]
            else:
                name = func.__name__

        tasks[name] = {"f": func, "o": options}

        return func

    return decorator


def default_task() -> t.Union[t.Callable, t.NoReturn]:
    for _, task in tasks.items():
        if task["o"].get("default"):
            return task
    
    return None


def get_task(target: t.Text) -> t.Mapping:
    for n, task in tasks.items():
        print(re.findall(n, target))
        if re.findall(n, target):
            return task


def exec_task(
    task: t.Union[t.Mapping, t.Text],
    args: t.Optional[t.Iterable] = []
) -> t.Any:
    if isinstance(task, t.Text):
        task: t.Mapping = get_task(task)

    rlist: t.Iterable = []
    opts: t.Mapping = task["o"]

    if opts.get("deps"):
        for i in opts["deps"]:
            try:
                tasks[i]["f"]()
            except KeyError:
                raise e.NoTaskFoundError(i)
    
    if opts.get("pattern"):
        rlist = re.findall(opts["pattern"], ' '.join(args))

    return task["f"](*rlist)
