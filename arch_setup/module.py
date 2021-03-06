from abc import ABC
from typing import TYPE_CHECKING, Iterable

from .package_manager import YayPackageManager

if TYPE_CHECKING:
    from .register import ModuleRegister


class Module(ABC):
    def __init__(self, name: str, desc: str) -> None:
        self.name = name
        self.desc = desc

        self._package_manager = YayPackageManager()

        self.packages = self.setup_packages()
        self.dependencies = self.setup_dependencies()

    def install(self, register: ModuleRegister) -> None:
        if not register.is_installed(self.name):
            for module in self.dependencies:
                module.install(register)

            self._package_manager.install(self.packages)

            self.config()
            register.set_installed(self.name)

    def config(self) -> None:
        pass

    def setup_dependencies(self) -> Iterable['Module']:
        return []

    def setup_packages(self) -> Iterable[str]:
        return []
