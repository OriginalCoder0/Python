"""
  自动化监控与报警
"""

import psutil
import time

class Monitor():

    cpu_data = []

    @classmethod
    def mem(cls, max=90):
        val = psutil.virtual_memory().percent
        if val > max:
            cls.send_msg('内存使用率为{:.1f}%，超过了{}%，请注意！'.format(val, max))

    @classmethod
    def cpu(cls, max=90):
        val = psutil.cpu_percent(1)

        cls.cpu_data.append(val)
        print(cls.cpu_data)

        if len(cls.cpu_data) >= 3:
            avg = sum(cls.cpu_data)/len(cls.cpu_data)

            if avg > max:
                cls.send_msg('CPU使用率为{:.1f}%，超过了{}%，请注意！'.format(avg, max))

            cls.cpu_data.pop(0)

    @classmethod
    def send_msg(cls, content):
        print(content)

    @classmethod
    def send_mail(cls, content):
        import smtplib

        nickname = '监控程序'
        sender   = '870179822@qq.com'
        password = ''
        receiver = 'luhuadong@163.com'
        pass

    @classmethod
    def send_wechat(cls, content):
        pass


while True:
    Monitor.mem(80)
    Monitor.cpu(2)
    time.sleep(1)

