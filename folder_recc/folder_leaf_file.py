from abc import ABC, abstractmethod

from folder_recc.folder_component import Component


class Composite(Component):

    def __init__(self, name):
        super().__init__(name)

    @abstractmethod
    def add_child(self, child: Component):
        self.children.append(child)

    @abstractmethod
    def remove_file(self, child: Component):
        self.children.remove(child)

    # @override
    # def get_size(self):
    #     return sum(file.get_size() for file in self.files)

    @abstractmethod
    def print(self, space):
        # folder_size = format_size(self.get_size())
        # print(space + self.name,folder_size)
        print(space, self.name)
        for file in self.children:
            file.print(space + 4 * " ")
