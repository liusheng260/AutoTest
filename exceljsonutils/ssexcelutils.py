#coding=utf-8

#对excel的常用操作进行封装
import xlrd
from xlutils.copy import copy

from data import ssglobal_var


class ssOperationExcel:
    # 获取excelsheet
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/case1.xls'
            self.sheet_id = 0
        self.data = self.get_data()


    #获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取某一个单元格的内容
    def get_cell_value(self,row,col):
        tables = self.data.cell_value(row,col)
        return tables

    #将实际结果 回写到excel用例中去
    #不能对已经存在的excel直接保存，可以对新建的excel进行保存
    #新建一份excel（复制原来的），覆盖保存
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        #定位sheet
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        #覆盖保存新建的excel文件
        write_data.save(self.file_name)

    #获取某一列的内容
    def get_cols_data(self,col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


    #根据case_id定位行号
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1

    #根据行号获取内容
    def get_row_values(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data


    #增加方法：根据 caseid用例号 去获取对应行的内容
    def get_rows_data(self,case_id):
        #1、根据case_id定位行号
        row_num = self.get_row_num(case_id)
        #2、根据行号获取内容
        rows_data = self.get_row_values(row_num)
        return rows_data

if __name__=="__main__":
    opers = ssOperationExcel()
    print(opers.get_cell_value(1,1))
