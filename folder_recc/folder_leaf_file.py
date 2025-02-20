from abc import ABC, abstractmethod
from typing import override

from folder_recc.folder_component import Component

class File(Component):

    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    @override
    def add_child(self, child: Component):
        raise NotImplementedError

    @override
    def remove_file(self, child: Component):
        raise NotImplementedError

    @override
    def get_size(self):
        return self.__size

    @override
    def set_size(self):
        pass

    @override
    def print(self, space):
        # folder_size = format_size(self.get_size())
        # print(space + self.name,folder_size)
        print(space, self.name, Component.format_size(self.__size))
