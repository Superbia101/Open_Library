from collections.abc import Generator
from os import chdir


def сhange_working_directory(path: str) -> Generator:
    """"""

    try:
        chdir(path)
        yield

    finally:
        chdir(path)


with сhange_working_directory('C:\\'):
    print(os.listdir())