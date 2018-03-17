#coding:utf-8
import json
import time
import hashlib
from exceljsonutils.ssjsonutils import OperationJson

class httpApi:
    def get_key(self,key='test'):
        return key

    def httpTime(self):
        t = int(time.time())
        #print(int(t))
        return t


    def create_sign(self):
        h = hashlib.md5()
        k = str(httpApi.get_key(self))
        t = str(httpApi.httpTime(self))
        h.update((k+t).encode('utf-8'))
        return h.hexdigest()
        #print(h.hexdigest())

    def http_curl(self):
        keys = str(httpApi.get_key(self))
        Time = str(httpApi.httpTime(self))
        #sign = str(httpApi.create_sign(self))
        return {"key":keys,"time":Time}
        #return {"key": keys, "time": Time,"sign":sign}
        #print({"key":keys,"time":Time,"sign":sign})

        jsonkey = json.dumps(keys,ensure_ascii=False)
        jsonTime = json.dumps(Time, ensure_ascii=False)
        jsonsign = json.dumps(sign, ensure_ascii=False)
        print(jsonkey,jsonTime,jsonsign)

        
        '''
        oper = OperationJson()
        oper.write_append_data({"key":keys,"time":Time,"sign":sign})
        
        #return oper
        #print(oper)
        '''

if __name__=='__main__':
    run = httpApi()
    run.httpTime()
    run.create_sign()
    run.http_curl()