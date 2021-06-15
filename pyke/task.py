import re

import typing as t

from pyke import tasks
from pyke import errors as e


def task(*args, **options: t.Any) -> t.Callable:
    r"""
    Function decorator to create a Pykefile task with a name 
    and certain options.

    :param name: Name of the task to be called from the ``pyke``
        command. If no name is given, the function name is used.
        If the task uses a regex ``pattern`` option, that pattern
        will used and matched against args passed to ``pyke``.
    :type name: `Text`, optional

    :options:
        * *default* (``bool``) -- 
            Setting to ``True`` will set the task as default. This
            task will run when ``pyke``  doesn't recieve any arguments.
        * *deps* (``Iterable[Text]``) -- 
            List of task names to run before the current task. Tasks
            that use patterns cannot be used as task dependencies.
        * *pattern* (``Text``, `valid regex`) -- 
            Regex pattern to match against args. All found matches 
            will be passed to the task function as string arguments.

    """
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
