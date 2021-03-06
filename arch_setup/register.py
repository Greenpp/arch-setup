class ModuleRegister:
    def __init__(self) -> None:
        self.installed = {}

    def is_installed(self, name: str) -> bool:
        flag = False
        if name in self.installed and self.installed[name]:
            flag = True

        return flag

    def set_installed(self, name: str) -> None:
        self.installed[name] = True
