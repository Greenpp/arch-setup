import subprocess
from typing import Iterable


class YayPackageManager:
    def __init__(self) -> None:
        self.name = 'yay'

    def install(self, packages: Iterable[str]) -> None:
        arguments = ['-S', '--noconfirm']

        subprocess.run([self.name, *arguments, *packages])

    def update(self) -> None:
        arguments = ['-Ssyu']

        subprocess.run([self.name, *arguments])
