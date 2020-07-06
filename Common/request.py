import requests
import json
from Common.logger import Logger
from Common.set_token import SetToken
import allure

logger = Logger(logger="request").getlog()


class RunMethod:
    @allure.step('获取数据发送请求')
    def post_main(self, url, data, header=None):
        headers = SetToken().set_token(header)
        logger.info('最终请求头：%s' % headers)
        logger.info('最终请求数据：%s' % data)
        res = requests.post(url=url, json=json.loads(data), headers=headers)
        lrt = res.text
        logger.info('响应数据：%s' % lrt)
        return lrt
        # return json.dumps(res, indent=2, ensure_ascii=False)

    def get_main(self, url, data, header=None):
        headers = SetToken().set_token(header)
        logger.info('最终请求头：%s' % headers)
        logger.info('最终请求数据：%s' % data)
        res = requests.get(url=url, json=json.loads(data), headers=headers)
        lrt = res.text
        logger.info('响应数据：%s' % lrt)
        return lrt
        # return json.dumps(res, indent=2, ensure_ascii=False)

    def run_main(self, method, url, id, info, data=None, header=None):
        logger.info('请求ID：%s' % int(id))
        logger.info('请求信息：%s' % info)
        logger.info('请求地址：%s' % url)
        logger.info('请求头：%s' % header)
        logger.info('请求数据：%s' % data)
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res
