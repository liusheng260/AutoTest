#coding:utf-8
import json
import time
import hashlib
import datetime
from exceljsonutils.ssjsonutils import OperationJson

class httpApi:
    def get_key(self,key='test'):
        if key == 'test':
            return 'test'
        else:
            return key

    def httpTime(self):
        t = int(time.time())
        #print(int(t))
        return t

    def get_app_secret1(self,app_secret1='test2017'):
        return app_secret1

    def get_datetime(self):
        today = datetime.date.today()
        #print(today)
        return today

    def get_app_key(self,app_key='23281515'):
        return app_key

    def get_format(self,format='json'):
        return format

    def get_sign_method(self,sign_method='hmac'):
        return sign_method

    def get_version(self,v='2.0'):
        return v

    def get_app_secret(self,app_secret='152e210bc9f87a2fdb00888a2abb30be'):
        return app_secret

    def get_customerId(self,customerId='devtest'):
        return customerId

    def get_target_app_key(self,target_app_key='23036663'):
        return target_app_key

    def get_method(self,method='taobao.pos.weborder.add'):
        return method

    def get_session(self,session='6101f30ed9c3a541a67bc7efba6a8bf4e4c6201416614252249787712'):
        return session

    def create_sign(self):
        #h = hashlib.md5()
        k = str(httpApi.get_key(self))
        s = str(httpApi.get_app_secret1(self))
        t = str(httpApi.get_datetime(self))
        ks = k.lower()+s.lower()
        #print("ks:"+ks)
        #print("kst:"+(ks+t))
        h = hashlib.md5((ks+t).encode('utf-8'))
        #h.update((k+s).encode('utf-8'))
        return h.hexdigest()
        #print(h.hexdigest())

    #奇门sign
    def create_sign2(self):
        #h = hashlib.md5()
        k = str(httpApi.get_app_key(self))
        t = str(httpApi.httpTime(self))
        f = str(httpApi.get_format(self))
        m = str(httpApi.get_method(self))
        v = str(httpApi.get_version(self))
        a = str(httpApi.get_app_secret(self))
        c = str(httpApi.get_customerId(self))
        ta = str(httpApi.get_target_app_key(self))
        s = str(httpApi.get_session(self))
        sm = str(httpApi.get_sign_method(self))
        adict = {"app_key":k,"timestamp":t,"format":f,"method":m,"version":v,"app_secret":a,"customerId":c,"target_app_key":ta,"session":s,"sign_method":sm}
        sort = str(sorted(adict.items(), key=lambda adict: adict[0]))
        #sort = str(httpApi.sortedDictValues1(adict))
        sign = ''
        for key,value in adict.items():
            if key!='' and value!='':
                sign =sign + key + value
        #print(sign)
        #return sign
        sort_sign = a+sign+a
        #print(sort_sign)
        #h.update(sort.encode('utf-8'))
        #print(h.hexdigest())
        h = hashlib.md5(sort_sign.encode('utf-8'))
        #print(h.hexdigest().upper())
        return h.hexdigest().upper()


    #ipos+
    def http_curl(self):
        keys = str(httpApi.get_key(self))
        Time = str(httpApi.httpTime(self))
        sign = str(httpApi.create_sign(self))
        return {"key": keys, "time": Time,"sign":sign}
        #print({"key":keys,"time":Time,"sign":sign})

        # jsonkey = json.dumps(keys,ensure_ascii=False)
        # jsonTime = json.dumps(Time, ensure_ascii=False)
        # jsonsign = json.dumps(sign, ensure_ascii=False)
        # print(jsonkey,jsonTime,jsonsign)

    #奇门
    def http_curl2(self):
        app_key = str(httpApi.get_app_key(self))
        timestamp = str(httpApi.httpTime(self))
        format = str(httpApi.get_format(self))
        method = str(httpApi.get_method(self))
        version = str(httpApi.get_version(self))
        app_secret = str(httpApi.get_app_secret(self))
        customerId = str(httpApi.get_customerId(self))
        target_app_key = str(httpApi.get_target_app_key(self))
        session = str(httpApi.get_session(self))
        sign_method = str(httpApi.get_sign_method(self))
        sign = str(httpApi.create_sign2(self))
        #print({"app_key": app_key, "timestamp": timestamp,"format":format,"method":method,"v":version,"app_secret":app_secret,"customerId":customerId,"target_app_key":target_app_key,"bill":bill,"session":session,"sign_method":sign_method})
        return {"app_key": app_key, "timestamp": timestamp,"format":format,"method":method,"v":version,"app_secret":app_secret,"customerId":customerId,"target_app_key":target_app_key,"session":session,"sign_method":sign_method,"sign":sign}

if __name__=='__main__':
    run = httpApi()
    #run.httpTime()
    run.get_datetime()
    run.create_sign()
    run.http_curl()
    #run.create_sign2()
    #run.http_curl2()