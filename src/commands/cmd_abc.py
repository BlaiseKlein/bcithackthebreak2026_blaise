from abc import ABC, abstractmethod

class Command(ABC):
    
    @abstractmethod
    def build_cmd(self):
        pass