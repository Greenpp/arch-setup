import subprocess
from abc import ABC, abstractmethod
from string import Template
from typing import TYPE_CHECKING, Iterable, Optional

if TYPE_CHECKING:
    from .manager import PackageManager


class Action(ABC):
    @abstractmethod
    def execute(self, **kwargs) -> None:
        pass


class CommandAction(Action):
    def __init__(
        self,
        command: str,
        as_root: bool = True,
        user: Optional[str] = None,
        group: Optional[str] = None,
        sync: bool = False,
    ) -> None:
        if not as_root and user is None:
            raise ValueError('No user specified for non root command')

        self.command = command.split()
        self.user = 'root' if as_root else user
        self.group = user if group is None else group
        self.sync = sync

    def execute(self, **kwargs) -> None:
        p = subprocess.Popen(self.command, user=self.user, group=self.group)
        if self.sync:
            p.wait()


class InstallAction(Action):
    def __init__(self, packages: Iterable[str], manager: PackageManager) -> None:
        self.packages = packages
        self.manager = manager

    def execute(self, **kwargs) -> None:
        self.manager.install(self.packages)


class TemplateAction(Action):
    def __init__(self, template_path: str, file_location: str) -> None:
        with open(template_path) as f:
            self.template = Template(f.read())

        self.file_location = file_location

    def execute(self, **kwargs) -> None:
        filled_template = self.template.substitute(kwargs)

        with open(self.file_location, 'w') as f:
            f.write(filled_template)
