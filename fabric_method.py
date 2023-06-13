from enum import Enum


class Chrome:
    def __init__(self):
        print("Get ChromeDriver")


class Firefox:
    def __init__(self):
        print("Get GeckoDriver")


class Edge:
    def __init__(self):
        print("Get EdgeDriver")


class MyEnum(Enum):
    CHROME = 1
    FIREFOX = 2
    EDGE = 3


def create_driver(driver_name: MyEnum):
    if driver_name == MyEnum.CHROME:
        return Chrome()
    elif driver_name == MyEnum.FIREFOX:
        return Firefox()
    elif driver_name == MyEnum.EDGE:
        return Edge()
    else:
        return Chrome()


create_driver(MyEnum.FIREFOX)
