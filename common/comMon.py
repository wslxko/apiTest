import xlrd
from readConfig import ReadConfig
from common import httpConfig
import readConfig
from common.Log import MyLog as Log
import json

proDir = readConfig.proDir
localReadConfig = readConfig.ReadConfig()
localConfigHttp = httpConfig.HttpConfig()
log = Log.get_log()
logger = log.get_logger()


class Common:
    # 从excel中读取测试用例
    def get_xls(self, sheetname):
        cls = []
        filepath = localReadConfig.getFile('testfile', 'testdata.xlsx')
        excel = xlrd.open_workbook(filepath)
        sheet = excel.sheet_by_name(sheetname)
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != 'case_name':
                cls.append(sheet.row_values(i))
        return cls

    # 从json中读取apiurl
    def getApiFromJson(self, api):
        filepath = localReadConfig.getFile('testfile', 'urls.json')
        with open(filepath) as file:
            filedata = file.read()
            dict_data = json.loads(filedata)
            return dict_data[api]

    def get_value_from_msg(self, info, key):
        return info[key]
