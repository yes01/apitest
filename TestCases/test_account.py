from Common.get_data import GetData
import pytest
import json
from Common.Yaml import Yaml
from Common.Assert import Assert
from Common.get_captcha import GetCaptcha
from Common.request import RunMethod
from Common.set_sql import SetSql
from Common.logger import Logger
import allure

logger = Logger(logger="account").getlog()


@allure.feature('账号模块')
class TestAccount:
    try:
        all_data = GetData().get_data('account')
    except:
        all_data = []

    @pytest.mark.parametrize('data', all_data,
                             ids=["接口序列：{}--->请求信息:{}".format(data['接口序列'], data['接口信息']) for
                                  data in all_data])
    def test_account(self, data):
        id, info, url, method, headers, api_data, expect = data['接口序列'], data['接口信息'], data['url'], data['请求方式'], data['请求头'], data['请求数据'], data['预期结果']
        Yaml().write_yaml_data('login.yaml',json.loads(api_data))
        body = GetCaptcha().get_captcha(api_data)
        res = RunMethod().run_main(method, url, id, info, body, headers)
        Assert().is_in(expect, res)
        SetSql().connect_database_update()


