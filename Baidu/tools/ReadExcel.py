import xlrd


class ReadExcel:
    def __init__(self, file, sheet):
        self.workbook = xlrd.open_workbook(file)
        self.sheet_name = self.workbook.sheet_by_name(sheet)

    def read_excel(self, row, col):
        value = self.sheet_name.cell(row, col).value
        if type(value) == float:
            value = str(int(value))
        return value


test_excel = ReadExcel('../data/test.xls', 'baidu')
value = test_excel.read_excel(0, 0)
print(value)
