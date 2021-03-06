import subprocess
from typing import Iterable

from ..module import Module


class PythonModule(Module):
    def __init__(self) -> None:
        name = 'Python'
        desc = 'Python development'

        super().__init__(name, desc)

    def config(self) -> None:
        # Poetry config
        # Create virtualenv in project directory
        command = 'poetry config virtualenvs.in-project true'
        subprocess.run(command.split())
        

    def setup_packages(self) -> Iterable[str]:
        packages = [
            'python',  # Latest version of python
            'python-poetry',  # Package and dependency manager
            'python-black',  # Linter
        ]

        return packages
