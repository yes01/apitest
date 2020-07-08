# -*- coding: UTF-8 -*-
import json
import requests
from Common.logger import Logger
from Common.Yaml import Yaml
from Common.config import ReadConfig
logger = Logger(logger="getcaptcha").getlog()


class GetCaptcha:
    def __init__(self):
        self.read_config = ReadConfig()
        self.url = self.read_config.get_TestUsers('url')
        self.url_logincaptcha = self.read_config.get_TestUsers('url_logincaptcha')

    def get_accessToken(self):
        try:
            bodys = self.get_accessTokenbody()
            res = requests.post(url=self.url, json=bodys).text
            res = json.loads(res)  # 转化为字典
            token = res["result"]["accessToken"]  # 拿到accessToken
            tokens = "Bearer " + token
            headers = dict(authorization=tokens)
            return headers
        except:
            logger.info('accessToken获取失败，请检查登录是否有效！')


    def get_captcha(self, api_data):
        try:
            Token = self.get_accessToken()
            bodys = self.get_captchabody()
            res = requests.post(url=self.url_logincaptcha, json=bodys, headers=Token).text
            res = json.loads(res)  # 转化为字典
            captcha = res["result"]["authenticationCode"]  # 拿到authenticationCode
            content = json.loads(api_data)
            content['authenticationCode'] = captcha
            return json.dumps(content)
        except:
            logger.info('验证码获取失败，请检查参数是否有效！')

    def get_accessTokenbody(self):
        data = Yaml().get_yaml_data('login.yaml')
        text = data['text']
        find = "@"
        if find in text:
            body = dict(text=text, password='12345678')
            return body

        else:
            countryCode = data['countryCode']
            body = dict(text=text, password='12345678', countryCode=countryCode)
            return body



    def get_captchabody(self):
        data = Yaml().get_yaml_data('login.yaml')
        text = data['text']
        scene = data['scene']
        find = "@"
        if find in text:
            body = dict(text=text, scene=scene)
            return body

        else:
            countryCode = data['countryCode']
            body = dict(text=text, scene=scene, countryCode=countryCode)
            return body










