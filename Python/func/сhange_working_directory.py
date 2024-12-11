from collections.abc import Iterable
from contextlib import contextmanager
from os import chdir, getcwd, listdir


@contextmanager
def сhange_working_directory(new_path: str) -> Iterable:
    """"""

    old_path = getcwd()
    try:
        chdir(new_path)
        yield

    finally:
        chdir(old_path)


with сhange_working_directory('C:\\') as a:
    print(listdir())