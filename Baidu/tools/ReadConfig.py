import configparser


class ReadConfig:
    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    def get_config(self, section, name):
        value = self.cf.get(section, name)
        return value
