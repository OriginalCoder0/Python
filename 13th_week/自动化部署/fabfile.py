from fabric.api import *
import datetime

env.user='root'
env.hosts=['192.168.88.176', '192.168.88.179']

def pack():
    """ 打包 """

    # 删除原来的压缩包
    local('rm -f temp.tar.gz')
    # 更新代码仓库
    local('cd project1 && git pull origin master')
    # 重新打包，并排除.git目录
    local('cd project1 && tar -czf ../temp.tar.gz --exclude=.git .')


def deploy():
    """ 部署 """

    # 远程的临时文件
    remote_temp_tar = '/tmp/temp.tar.gz'
    run('rm -rf ' +  remote_temp_tar)
    # 传输文件
    put('temp.tar.gz', remote_temp_tar)

    # 每次发布解压到不同的目录，以区分版本
    tag = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    remote_dist_dir ='/data/deploy/project1@' + tag
    run('mkdir -p '+ remote_dist_dir)

    with cd(remote_dist_dir) :
        run('tar -zxf ' +  remote_temp_tar)

    # 删除并重新创建软链接
    run('mkdir -p /data/webroot')
    link = '/data/webroot/project1'
    run('rm -f ' + link)
    run('ln -s %s %s' % (remote_dist_dir, link))

    # 重启uwsgi
    with settings(warn_only=True):
        run('pkill uwsgi')
        run('/usr/local/bin/uwsgi --ini /data/uwsgi.ini')

