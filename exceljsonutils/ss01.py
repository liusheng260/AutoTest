#coding:utf-8
#读取excel中的数据
import xlrd
#打开excel文件
data = xlrd.open_workbook('../dataconfig/case1.xls')
#定位sheet
tables = data.sheets()[0]
print(tables.cell_value(2,3))

#封装成工具类
#  excel  的API ： 如下
#操作excel的API小结：
#xlrd:
#open_workbook(文件名)  打开文件名
#文件.sheets()[sheet的id编号]  根据id获取编号
#sheet表.nrows  获取行数
#sheet表.cell_value(row,col)  根据行列定位单元格值
#sheet表.col_values(col_id)  根据列号获取数据

#xlwt:
#文件get_sheet(id号)
#sheet表.write(行，列，覆盖新额内容)
#文件.save(self.file_name)保存
#xlutils：
#copy 用于复制excel

