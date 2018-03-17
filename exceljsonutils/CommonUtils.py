#coding:utf-8
class CommonUtils:
    def is_contains(self,str_one,str_two):
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag