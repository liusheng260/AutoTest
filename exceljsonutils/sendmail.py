#coding:utf-8
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global send_user
    global email_host
    global password

    email_host = "smtp.mxhichina.com"
    send_user = "sheng.liu@baisonmail.com"
    password = "ls123456!!"

    def send_email(self,user_list,sub,content):
        user = "ss"+"<"+send_user+">"
        message = MIMEText(content,_subtype='plain',_charset='UTF-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)

        #使用smtp服务
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main2(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num+fail_num

        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" %(fail_num/count_num*100)
        user_list = ['1275254257@qq.com']
        sub = "接口自动化测试报告"
        content = "此次共运行接口数为%s个，通过数为%s个，失败数为%s个，通过率为%s，失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_email(user_list,sub,content)



if __name__=='__main__':
    send = SendEmail()
    user_list = ['1275254257@qq.com']
    sub = "测试邮件"
    content = "This is a first test email!"
    send.send_email(user_list,sub,content)
