#coding:utf-8
from data import ssglobal_var
from exceljsonutils.ssexcelutils import ssOperationExcel
from exceljsonutils.ssjsonutils import OperationJson


class ssGetData:
    #工具类初始化
    def __init__(self):
        self.opera_excel = ssOperationExcel()

    #获取excel行号==用例的个数
    def get_case_line(self):
        return self.opera_excel.get_lines()
    #获取是否执行
    def get_is_run(self,row):
        #列号
        col = int(ssglobal_var.get_run())
        flag = None
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model=='yes':
            flag=True
        else:
            flag=False
        return flag

    #获取是否携带header
    def is_header(self,row):
        # 列号
        col = int(ssglobal_var.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return header
        else:
            return None
    #获取请求方式
    def get_request_method(self,row):
        col = int(ssglobal_var.get_run_way())
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    #获取url
    def get_requests_url(self,row):
        col = int(ssglobal_var.get_url())
        url = self.opera_excel.get_cell_value(row,col)
        return url

    #获取请求数据 --- 关键字
    def get_request_data(self,row):
        col = int(ssglobal_var.get_data())
        data = self.opera_excel.get_cell_value(row,col)
        if data =='':
            return None
        else:
            return data

    #通过关键字到json文件中取出对应内容 作为请求的数据
    def get_data_for_json(self,row):
        oper_json = OperationJson()
        request_data = oper_json.get_data(self.get_request_data(row))
        return request_data

    #获取预期结果
    def get_except_data(self,row):
        col = int(ssglobal_var.get_expect())
        expect = self.opera_excel.get_cell_value(row,col)
        if expect =='':
            return None
        return expect

    #写入实际结果
    def write_result(self,row,value):
        col = int(ssglobal_var.get_result())
        self.opera_excel.write_value(row,col,value)

    #获取依赖返回数据的key
    def get_dependent_key(self,row):
        col = int(ssglobal_var.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key
    #判断使用需要用例依赖
    def is_depend(self,row):
        col = int(ssglobal_var.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row,col)
        if depend_case_id =="":
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(ssglobal_var.get_field_depend())
        data = self.opera_excel.get_cell_value(row,col)
        if data == "":
            return None
        else:
            return data

