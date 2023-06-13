from txt_writer import TxtWriter
from txt_reader import TxtReader


class Proxy:
    def __init__(self, txt_reader: TxtReader, text_writer: TxtWriter):
        self.__result = ''
        self.__is_actual = False
        self.__reader = txt_reader
        self.__writer = text_writer

    def write_file(self, new_data: str):
        self.__is_actual = False
        self.__writer.write_file(new_data)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        self.__result = self.__reader.read_file()
        self.__is_actual = True
        return self.__result


txt_reader = TxtReader("users.txt")
txt_writer = TxtWriter("users.txt")

proxy = Proxy(txt_reader, txt_writer)
print(proxy.read_file())
print('\n')
print(proxy.read_file())
print('\n')
proxy.write_file("new_data")
print(proxy.read_file())
