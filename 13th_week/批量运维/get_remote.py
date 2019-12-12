"""

"""

import paramiko
import psutil

CMD = {
    'cpu_cnt_phy': 'cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l',
    'cpu_cnt_log': 'cat /proc/cpuinfo | grep "processor" | wc -l',
    'cpu_info'   : 'cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c | sed "s/^[ \t]*//g"',
    'mem_stat'   : 'free -m',
    'disk_stat'  : 'df -h'
}

ssh = paramiko.SSHClient()

# 避免连接未知主机时出错
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def exec_remote_cmd(cmd):
    """ 执行远程命令 """

    stdin, stdout, stderr = ssh.exec_command(cmd)
    res = stdout.read().decode()
    return res


def main():
    """ 主程序 """

    ssh.connect(hostname="120.78.197.79", username="root", password="")

    print("CPU型号：" + exec_remote_cmd(CMD['cpu_info']))
    print("CPU物理核数：" + exec_remote_cmd(CMD['cpu_cnt_phy']))
    print("CPU逻辑核数：" + exec_remote_cmd(CMD['cpu_cnt_log']))

    print('-'*64)

    #cmd = "free -m"
    #cmd = "free -m | awk '/^Mem/{print $7}'"
    print(exec_remote_cmd(CMD['mem_stat']))

    print('-'*64)

    #cmd = "df -h"
    print(exec_remote_cmd(CMD['disk_stat']))


# 主程序入口
if __name__ == '__main__':
    main()
