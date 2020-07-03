# -*- coding: UTF-8 -*-
import json
from Common.logger import Logger
from Common.get_token import GetToken
logger = Logger(logger="settoken").getlog()


class SetToken:

    def set_token(self, header):
        if header is None:
            logger.info('请求头：%s' % header)
        else:
            content = json.loads(header)
            text = content.get('authorization')
            t = GetToken().get_token()
            headers = text + t
            content['authorization']=headers

            return content
