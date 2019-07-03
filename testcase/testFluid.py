from common.comMon import Common
import paramunittest
import unittest
from common.Log import MyLog
from common.httpConfig import HttpConfig
import json

common = Common()
data_xls = common.get_xls('spuForFulid')
localConfigHttp = HttpConfig()


@paramunittest.parametrized(*data_xls)
class SpuForFulidCase(unittest.TestCase):
    def setParameters(self, case_name, input, code):
        self.case_name = case_name
        # eval用于去掉字符串的引号
        self.input = eval(input)
        self.code = code
        self.response = None
        self.info = None

    def setUp(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def tearDown(self):
        pass

    def test_fulid(self):
        self.apiurl = common.getApiFromJson('checkSkuForFulid')
        localConfigHttp.set_url(self.apiurl)
        data = {
            "upcs": self.input
        }
        print(data)
        localConfigHttp.set_data(data)
        self.response = localConfigHttp.postWithJson()
        print(self.response.text)
        self.checkResult()

    def checkResult(self):
        self.info = self.response.json()
        code = common.get_value_from_msg(self.info, 'code')
        self.assertEqual(code, self.code, '断言失败')


if __name__ == '__main__':
    unittest.main()
