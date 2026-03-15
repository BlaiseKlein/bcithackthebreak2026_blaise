from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def parse(self, ui_dict):
        pass
    
    @abstractmethod
    def build_cmd(self):
        pass

    @abstractmethod
    async def run_cmd(self):
        pass