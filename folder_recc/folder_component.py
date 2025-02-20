from abc import ABC, abstractmethod

class Component(ABC):

    def __init__(self, name: str):
        self.name: str = name
        self.__size = None

    @staticmethod
    def format_size(size_in_bytes):
        """Convert bytes to human-readable format (KB, MB, GB)."""
        if size_in_bytes < 1024:
            return f"{size_in_bytes} B"
        elif size_in_bytes < 1024 ** 2:
            return f"{size_in_bytes / 1024:.2f} KB"
        elif size_in_bytes < 1024 ** 3:
            return f"{size_in_bytes / (1024 ** 2):.2f} MB"
        else:
            return f"{size_in_bytes / (1024 ** 3):.2f} GB"

    @abstractmethod
    def add_child(self, child):
        raise NotImplementedError

    @abstractmethod
    def remove_file(self, child):
        raise NotImplementedError

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def set_size(self):
        pass

    @abstractmethod
    def print(self, space):
        pass

    # @abstractmethod
    # def get_size(self):
    #     pass
