class FromTxtToJsonAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def convert_from_txt_to_json(self):
        with open(self.__file_path) as file:
            lines = file.readlines()
        headers_txt = lines[0]
        print(headers_txt)
        data_txt = lines[1:]
        print(data_txt)
        headers = headers_txt.replace('\n', '').split(',')
        print(headers)
        data = [item.replace('\n', '').split(',') for item in data_txt]
        print(data)
        result = []
        for item in data:
            result.append(dict(zip(headers, item)))
        print(result)


if __name__ == '__main__':
    FromTxtToJsonAdapter("users.txt").convert_from_txt_to_json()