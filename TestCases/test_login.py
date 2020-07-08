from Common.get_data import GetData
import pytest
from Common.Assert import Assert
from Common.request import RunMethod
from Common.logger import Logger
import allure

logger = Logger(logger="login").getlog()


@allure.feature('登录模块')
class TestLogin:
    try:
        all_data = GetData().get_data('login')
    except:
        all_data = []

    @pytest.mark.parametrize('data', all_data,
                             ids=["接口序列：{}--->请求信息:{}".format(data['接口序列'], data['接口信息']) for
                                  data in all_data])
    def test_login(self, data):
        id, info, url, method, headers, api_data, expect = data['接口序列'], data['接口信息'], data['url'], data['请求方式'], data['请求头'], data['请求数据'], data['预期结果']
        res = RunMethod().run_main(method, url, id, info, api_data, headers)
        Assert().is_in(expect, res)


