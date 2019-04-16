import os
from datetime import datetime


class Empty:
    def __init__(self):
        self.empty_folders = []
        self.sub_folders = []

    def get_empty_folders_list(self, folders):
        empty_folders = []
        for folder in folders:
            for (root, directory, files) in os.walk(folder, topdown=True):
                root = os.path.normpath(root)
                if not directory and not files and root not in empty_folders:
                    empty_folders.append(root)
                # for d in dir:
                #     sub_folder.append(os.path.normpath(os.path.join(root, d)))
                #     if root in sub_folder:
                #         sub_folder.remove(root)
            # print(sub_folder)

        empty_list = self.make_list(empty_folders)
        return empty_list

    def make_list(self, empty_folders):
        empty = []
        for folder in empty_folders:
            created_time = datetime.fromtimestamp(os.path.getctime(folder)).strftime('%Y-%m-%d %H:%M:%S')
            folder_details = list()
            folder_details.append(folder.split("\\")[-1])
            folder_details.append(folder)
            folder_details.append(str(created_time))
            folder_details.append('-')
            empty.append(folder_details)

        return empty

    def listdir_fullpath(self, folder):
        return [os.path.join(folder, file).replace('\\', '/') for file in os.listdir(folder)]
