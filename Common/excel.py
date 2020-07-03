import xlrd
from Common.logger import Logger

logger = Logger(logger="excel").getlog()


class Excel:
    def __init__(self):
        self.test_data_path = '../TestData/interface.xlsx'

    def open_excel(self, file):
        data = xlrd.open_workbook(file)
        return data

    def excel_table(self, file, sheetName):
        data = self.open_excel(file)
        # 通过工作表名称，获取到一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取行数
        Trows = table.nrows
        # 获取 第一行数据
        Tcolnames = table.row_values(0)
        lister = []
        for rownumber in range(1, Trows):
            row = table.row_values(rownumber)
            if row:
                app = {}
                for i in range(len(Tcolnames)):
                    app[Tcolnames[i]] = row[i]
                lister.append(app)
        return lister

    def get_list(self, sheetname):  # 获取整表的内容
        try:
            logger.info('开始解析 %s 表格的数据...' % sheetname)
            data_list = self.excel_table(self.test_data_path, sheetname)
            assert len(data_list) >= 0, u'excel标签页:' + sheetname + u'为空'
            return data_list
        except:
            logger.info('解析失败！！！')
            logger.info('未找到 %s 这个表格，请检查表格是否存在！！！' % sheetname)
