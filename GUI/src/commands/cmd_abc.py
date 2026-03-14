from abc import ABC, abstractmethod

class Command(ABC):
    
    @abstractmethod
    def build_cmd(self):
        pass

    def run_cmd(cmd_tool, cmd_name):
        cmd = cmd_tool.build_cmd()
        execute(cmd_name, cmd, print)