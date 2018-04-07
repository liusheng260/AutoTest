#coding:utf-8

#在非pycharm环境下 可以找关联模块
import sys
sys.path.append("/Users/liusheng/PycharmProjects/AutoTest")

from base.runmethod import RunMethod
from data.depend_data import DependdentData
from data.ssGetData import ssGetData
from exceljsonutils.CommonUtils import CommonUtils
from exceljsonutils.sendmail import SendEmail
from exceljsonutils.ssHttpApi import httpApi

class RunTest:
    #初始化工作
    def __init__(self):
        #模拟请求对象
        self.run_method = RunMethod()
        #获取excel和json数据
        self.data = ssGetData()
        self.api = httpApi()
        #比较规则
        self.com_util = CommonUtils()
        #初始化邮件对象
        self.send_mail = SendEmail()

    #运行工作
    #i充当的是行的作用
    def go_on_run(self):
        #定义两个列表
        pass_count=[]
        fial_count=[]

        #获取用例的个数
        rows_count = self.data.get_case_line()
        for i in range(1,rows_count):
            #获取某条用例的具体信息
            url = self.data.get_requests_url(i)
            method = self.data.get_request_method(i)
            isrun = self.data.get_is_run(i)
            #获取关键词对应的json数据
            request_data1 = self.data.get_data_for_json(i)
            #print(request_data1)
            request_data2 = self.api.http_curl()
            #request_data2 = self.api.http_curl2()
            #print(request_data2)
            request_data = dict(request_data1)
            request_data.update(request_data2)
            #print(request_data)


            #获取预期结果
            expect = self.data.get_except_data(i)
            header = self.data.is_header(i)
            if isrun:
                #判断是否需要依赖规则
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    #获取依赖的响应数据
                    self.dependdata = DependdentData(depend_case)
                    #获取依赖的响应数据
                    depend_response_data = self.dependdata.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    #添加依赖字段给 12 号的请求数据
                    #例子： 将depend_response_data（error_code的响应数据)存放到trade_number 所对应的值中去
                    request_data[depend_key] = depend_response_data

                res = self.run_method.run_main(method,url,request_data)
                print("实际结果",res)
                if self.com_util.is_contains(expect,res):

                    print("测试通过")
                    self.data.write_result(i,"测试通过")
                    pass_count.append(i)
                else:
                    print("测试失败")
                    self.data.write_result(i,"测试失败")
                    fial_count.append(i)
        print("成功的个数：",len(pass_count))
        print("失败的个数：",len(fial_count))
        self.send_mail.send_main2(pass_count,fial_count)

if __name__=='__main__':
    run = RunTest()
    run.go_on_run()
