import subprocess
from abc import ABC, abstractmethod
from typing import Iterable

from .action import CommandAction


class PackageManager(ABC):
    @abstractmethod
    def install(self, packages: Iterable[str]) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass


class PacmanPackageManager(PackageManager):
    def install(self, packages: Iterable[str]) -> None:
        command = 'pacman -S --noconfirm ' + ' '.join(packages)
        action = CommandAction(command)
        action.execute()

    def update(self) -> None:
        command = 'pacman -Syu'
        action = CommandAction(command)
        action.execute()


class YayPackageManager(PackageManager):
    def install(self, packages: Iterable[str]) -> None:
        command = 'yay -S --noconfirm ' + ' '.join(packages)
        action = CommandAction(command)
        action.execute()

    def update(self) -> None:
        command = 'yay -Syu --noconfirm'
        action = CommandAction(command)
        action.execute()
