import requests
from readConfig import ReadConfig
from common.Log import MyLog as Log

localReadConfig = ReadConfig()


class HttpConfig:
    def __init__(self):
        global baseurl, timeout
        baseurl = localReadConfig.getIniConfig('HTTP', 'baseurl')
        timeout = localReadConfig.getIniConfig('HTTP', 'timeout')
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.data = {}
        self.params = {}
        self.url = None

    def set_url(self, apiurl):
        self.url = baseurl + apiurl
        return self.url

    def set_header(self, header):
        self.header = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error('time out!')
            return None

    def postWithJson(self):
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error('time out!')
            return None

    def get(self):
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error('time out!')
            return None
