#coding=utf-8

#json 转换成字典来使用
import json

fp = open("../dataconfig/jw1.json",encoding='UTF-8')
#加载句柄
data = json.load(fp)
print(data['addcart'])
