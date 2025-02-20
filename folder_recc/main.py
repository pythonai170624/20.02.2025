import os
from folder_composite import *
from folder_leaf_file import *

def list_files_recc(folder_path) -> "Composite":
    current_folder = Folder(folder_path)

    for item in os.listdir(folder_path):

        full_path = os.path.join(folder_path, item)

        if os.path.isdir(full_path):
            # FOLDER
            folder_comp = list_files_recc(full_path)
            current_folder.add_child(folder_comp)
        else:
            # FILE
            size = os.path.getsize(full_path)
            file = File(item, size)
            current_folder.add_child(file)

    return current_folder

#root = list_files_recc(r"d:\test")
root = list_files_recc(r"d:\test\easy")
root.set_size()  # not recursive
root.print('')
