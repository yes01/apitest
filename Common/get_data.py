from Common.excel import Excel
# from Common.random_phone import RandomPhone
from Common.logger import Logger

logger = Logger(logger="getdata").getlog()


class GetData:
    def get_data(self, sheetname):
        all_data = Excel().get_list(sheetname)  # 获取excel里面的全部测试用例
        excute_data = []  # 准备一个空列表，装入标识为'yes'的测试用例，代表需要执行
        for item in all_data:
            if item['是否执行'] == 'yes':  # 判断是否需要执行
                if str(item).find('${phone}') != -1:  # 判断是否替换手机号码（每次注册都需要不同的号码，专门为注册接口准备）
                    # item = str(item).replace('${phone}', RandomPhone().CreatePhone())  # 将手机号码替换为随机生成的未注册的号码
                    item = eval(item)
                    excute_data.append(item)
                else:
                    excute_data.append(item)
        logger.info('%s 表格本次允许执行的用例个数为%s' % (sheetname, len(excute_data)))
        return excute_data
