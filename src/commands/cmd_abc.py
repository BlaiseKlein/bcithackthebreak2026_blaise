from abc import ABC, abstractmethod
from executor import execute

class Command(ABC):

    @abstractmethod
    def parse(self, ui_dict):
        pass
    
    @abstractmethod
    def build_cmd(self):
        pass

    def run_cmd(cmd_tool, cmd_name):
        cmd = cmd_tool.build_cmd()
        execute(cmd_name, cmd, print)