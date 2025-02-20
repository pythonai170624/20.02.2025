from abc import ABC, abstractmethod
from typing import override

from folder_recc.folder_component import Component


class Folder(Component):

    def __init__(self, name):
        super().__init__(name)
        self.__size = 0
        self.children = []

    @override
    def add_child(self, child: Component):
        self.children.append(child)

    @override
    def remove_file(self, child: Component):
        self.children.remove(child)

    @override
    def get_size(self):
        return self.__size

    @override
    def set_size(self):
        for child in self.children:
            child.set_size()
        self.__size = sum(child.get_size() for child in self.children)

    @override
    def print(self, space):
        print(space + self.name, Component.format_size(self.__size))
        for file in self.children:
            file.print(space + 4 * " ")
