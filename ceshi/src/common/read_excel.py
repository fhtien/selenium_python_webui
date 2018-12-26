import xlrd
# from bases.config import TEST_DATA

'''
读取excel文件
'''


class excel:

    def open_excel(self,file):
        '''读取excel文件'''
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as  e:
            raise e

    def excel_table(self,file, sheetName):
        '''装载list'''
        data = self.open_excel(file)
        # 通过工作表名称，获取到一个工作表
        table = data.sheet_by_name(sheetName)
        # 获取总行数
        rowNum = table.nrows
        #获取总列数
        colNum = table.ncols
        # 获取 第一行数据
        keys = table.row_values(0)
        lister = []
        j = 1
        for i in range(rowNum - 1):
            s = {}
            # 从第二行取对应values值
            values = table.row_values(j)
            for x in range(colNum):
                s[keys[x]] = values[x]
            lister.append(s)
            j += 1
        return lister

    def get_list(self,sheetname):
        try:
            data_list = self.excel_table(TEST_DATA, sheetname)
            assert len(data_list)>=0,'excel标签页:'+sheetname+'为空'
            return data_list
        except Exception as e:
            raise e