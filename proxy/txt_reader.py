class TxtReader:
    def __init__(self, file_path):
        self.__file_path = file_path

    def read_file(self):
        with open(self.__file_path) as file:
            text = file.readlines()

        return text
