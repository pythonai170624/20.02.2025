from abc import ABC, abstractmethod

class Component(ABC):

    def __init__(self, name: str):
        self.name: str = name

    @abstractmethod
    def add_child(self, item):
        pass

    @abstractmethod
    def remove_child(self, item):
        pass

    @abstractmethod
    def get_file(self):
        pass

    @abstractmethod
    def draw(self, space):
        pass

    @abstractmethod
    def get_size(self):
        pass
