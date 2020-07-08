# -*- coding: UTF-8 -*-
import json
from Common.logger import Logger
from Common.get_token import GetToken
from Common.get_captcha import GetCaptcha
logger = Logger(logger="settoken").getlog()


class SetToken:

    def set_token(self, header, body):
        if header == 'None':
            if 'authenticationCode' in body:
                headerss = GetCaptcha().get_accessToken()
                return headerss
            else:
                logger.info('请求头111：%s' % header)
        else:
            content = json.loads(header)
            text = content.get('authorization')
            t = GetToken().get_token()
            headers = text + t
            content['authorization']=headers
            return content
