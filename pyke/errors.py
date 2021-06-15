class NoPykefileFound(Exception):
    """Could not find a valid `Pykefile` in the current directory."""

    def __str__(self):
        return "Could not find a valid `Pykefile` in the current directory."

class NoTaskFoundError(Exception):
    """Could not find given task name."""

    def __str__(self):
        return "Could not find given task name."


class NoDefaultTaskError(Exception):
    """No default task has been specified."""

    def __str__(self):
        return "No default task has been specified."
