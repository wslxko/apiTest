from configparser import ConfigParser
import os

proDir = os.path.split(os.path.abspath(__file__))[0]
filePath = os.path.join(proDir, 'config.ini')


class ReadConfig:
    def __init__(self):
        self.proDir = os.path.split(os.path.abspath(__file__))[0]
        self.config = ConfigParser()
        self.config.read(filePath)

    def getIniFile(self):
        filePath = os.path.join(self.proDir, 'config.ini')
        return filePath

    def getIniConfig(self, section, option):
        value = self.config.get(section, option)
        return value

    def set_header(self, option, value):
        self.config.set('HEADER', option, value)
        with open(filePath, 'w') as f:
            self.config.write(f)

    def getFile(self, path, file):
        proDir = os.path.split(os.path.abspath(__file__))[0]
        filePath = os.path.join(proDir, path, file)
        return filePath

    def get_email(self, name):
        value = self.config.get('EMAIL', name)
        return value
