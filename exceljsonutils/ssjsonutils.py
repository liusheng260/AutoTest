#coding=utf-8
import json


class OperationJson:
    #初始化步骤，构造函数
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path='../dataconfig/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        #with结构 可以自动关闭文件
        with open(self.file_path,encoding='utf-8') as fp:
            data = json.load(fp)
            return data


    #根据关键字获取对应的json数据
    def get_data(self,id):
        return self.data[id]

    #写入数据到json文件 --覆盖写
    def write_data(self,data):
        with open(self.file_path,'w',encoding='utf-8') as fp:
            #将json数据写入内容
            fp.write(json.dumps(data,ensure_ascii=False))

    #追加写
    def write_append_data(self,data):
        #将json 中数据遍历 是否传入的健
        with open(self.file_path,'r',encoding='UTF-8') as fp:
            #model已经存在的数据
            model = json.load(fp)
            for i in data:
                #如果是新的健 追加
                #如果是存在健 覆盖
                model[i] = data[i]

            #将model重新转转换为json
            jsobj = json.dumps(model,ensure_ascii=False)
        with open(self.file_path,'w',encoding='utf-8') as fp:
            fp.write(jsobj)

'''
if __name__=="__main__":
    opjson = OperationJson()
    opjson.write_append_data({"key":"jsonkey","time":"jsonTime","sign":"jsonsign"})
    opjson.write_append_data({"name":"李小璐"})
    opjson.write_append_data({"tool":{"namea":"锄头","nameb":"镰刀"}})
'''

