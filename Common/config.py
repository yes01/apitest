import codecs
import configparser
from Common.logger import Logger
from Common import all_path

logger = Logger(logger="config").getlog()
configPath = all_path.config_path


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w", encoding='UTF-8')
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_TestUsers(self, name):
        value = self.cf.get('TestUsers', name)
        return value

