from Common.logger import Logger
import allure
logger = Logger(logger="assert").getlog()


class Assert:
    @allure.step('返回响应数据进行断言')
    def is_in(self, expect_result, actual_result):
        logger.info('期待结果：%s' % expect_result)
        if expect_result in actual_result:
            logger.info('断言成功！')
        else:
            logger.info('断言失败！')
        assert expect_result in actual_result, '判断%s是否被包含在%s里面,当前断言失败' % (expect_result, actual_result)

    def is_equal(self, expect_result, actual_result):
        assert expect_result == actual_result, '判断%s是否等于%s,当前断言失败' % (expect_result, actual_result)

    def is_true(self, result):
        assert result, '判断%s是否为真,当前断言失败' % (result)

    def is_false(self, result):
        assert not result, '判断%s是否为假,当前断言失败' % (result)
