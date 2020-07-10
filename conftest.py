import pytest
import os
import sys
from py._xmlgen import html
from Common.logger import Logger
from Common.get_token import GetToken
logger = Logger(logger="conftest").getlog()


def pytest_configure(config):
    # 添加接口地址与项目名称
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    config._metadata["项目名称"] = "web接口自动化测试"


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 研发部平台组")])
    prefix.extend([html.p("测试人员: 李翔")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.pop(-1)  # 删除link列


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.pop(-1)  # 删除link列


@pytest.fixture(scope='session')
def token(request):
    t = GetToken().get_token()
    logger.info('-' * 20 + '开始执行测试用例' + '-' * 20)

    def final():
        logger.info('-' * 20 + '执行测试用例结束' + '-' * 20)

    request.addfinalizer(final)

    return t
