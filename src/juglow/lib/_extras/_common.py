from ..._exceptions import JuglowError

INSTRUCTIONS = """

Juglow error: missing required dependency `{library}`.

    $ pip install Juglow[{extra}]
"""


class MissingDependencyError(JuglowError):
    def __init__(self, *, library: str, extra: str) -> None:
        super().__init__(INSTRUCTIONS.format(library=library, extra=extra))
