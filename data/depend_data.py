#coding:utf-8
import json

from base.runmethod import RunMethod
from data.ssGetData import ssGetData
from exceljsonutils.ssexcelutils import ssOperationExcel
from jsonpath_rw import parse


class DependdentData:
    #通过case_id获取整行内容
    #初始化工作
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = ssOperationExcel()
        self.data = ssGetData()


    #根据caseid获取出整行的内容
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    #执行上一条用例的测试 获取结果
    def run_dependent(self):
        run_method = RunMethod()
        #获取用例行号
        row_num = self.opera_excel.get_row_num(self.case_id)
        #根据关键字获取json数据
        request_data = self.data.get_data_for_json(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_requests_url(row_num)
        res = run_method.run_main(method,url,request_data)
        return json.loads(res)


    #根据key键 获取响应的内容
    def get_data_for_key(self,row):
        depend_data = self.data.get_dependent_key(row)
        #获取被依赖用例的响应
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        if madle:
            return [math.value for math in madle][0]

