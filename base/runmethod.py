#coding:utf-8
import json

import requests

class RunMethod:
    #定义方法 判断返回的数据是否是json数据
    def check_json_format(self,raw_msg):
        #判断是否是字符串
        if isinstance(raw_msg,str):
            try:
                #如果不是字符串 报异常
                json.loads(raw_msg,encoding='utf-8')
            except ValueError:
                return False
            return True
        else:
            return False

    #模拟POST请求   目标获取结果
    def post_main(self,url,data,header=None):
        res = None
        if header!=None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        if self.check_json_format(res.text):
        #如果返回的是json
            print("实际响应结果",res.json())
            return res.json()
        else:
            print("实际响应结果",res.text)
            return res.text

    #模拟GET请求
    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,data=data,headers=header,verify=False)
        else:
            res = requests.get(url=url,data=data,verify=False)
        if self.check_json_format(res.text):
        #如果返回的是json
            print("实际响应结果",res.json())
            return res.json()
        else:
            print("实际响应结果",res.text)
            return res.text

    #合并两个方法的调用
    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
            # 以json结果返回初始数据
        return json.dumps(res,ensure_ascii=False)
