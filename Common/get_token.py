from Common.config import ReadConfig
import json
import requests
from Common.base import Base
from Common.logger import Logger


logger = Logger(logger="gettoken").getlog()


class GetToken:
    def __init__(self):
        self.read_config = ReadConfig()
        self.url = self.read_config.get_TestUsers('url')
        self.data = self.read_config.get_TestUsers('data')

    def get_token(self):
        logger.info('-' * 50)
        logger.info('准备前置条件：')
        logger.info('1.开始获取accessToken')
        try:
            res = requests.post(url=self.url, json=json.loads(self.data)).text
            res = json.loads(res)  # 转化为字典
            token = res["result"]["accessToken"]  # 拿到accessToken
            logger.info('2.获取accessToken成功')
            return token
        except:
            logger.info('2.accessToken获取失败，请检查登录是否有效！')

