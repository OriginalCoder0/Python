from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator

from monitor.models import Host, User
from datetime import datetime
# 验证密码
import hashlib


# Create your views here.

def index(request, pIndex=1):
    ''' 监控中心-首页 '''

    # return HttpResponse("Hello, world. You're at the myapp index.")

    # hostList = Host.objects.all()
    hostList = Host.objects.get_queryset().order_by('id')

    # 分页
    p = Paginator(hostList, 6)
    if pIndex == "":
        pIndex = "1"
    aList = p.page(pIndex)
    pList = p.page_range
    pNum = p.num_pages
    context = {"hostlist": aList, "pList": pList, "pIndex": int(pIndex), "pNum": int(pNum)}
    print('-' * 12)
    print(context)

    return render(request, "monitor/index.html", context)


def add(request):
    ''' 添加远程主机 '''
    return render(request, 'monitor/add.html')


def insert(request):
    ''' 执行远程主机添加操作 '''

    try:
        ob = Host()
        ob.tag = request.POST['tag']
        ob.ip = request.POST['ip']
        ob.cdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ob.save()
        print('添加成功！')
    except Exception as err:
        print(err)
        print('添加失败！')

    return redirect(reverse('index'))


def delete(request, hid):
    ''' 执行远程主机删除 '''
    try:
        ob = Host.objects.get(id=hid)
        ob.delete()
        print('删除成功！')
    except Exception as err:
        print(err)
        print('删除失败！')

    return redirect(reverse('index'))


def edit(request, hid):
    ''' 编辑远程主机信息 '''
    try:
        ob = Host.objects.get(id=hid)
        context = {'host': ob}
        return render(request, "monitor/edit.html", context)
    except Exception as err:
        print(err)
        print('没有找到要修改的信息！')
        return redirect(reverse('index'))


def update(request, hid):
    ''' 执行远程主机信息更新 '''
    try:
        ob = Host.objects.get(id=hid)
        ob.tag = request.POST['tag']
        ob.ip = request.POST['ip']
        ob.cpu = request.POST['cpu']
        ob.mem = request.POST['mem']
        ob.disk = request.POST['disk']
        ob.save()
        print('修改成功！')
    except Exception as err:
        print(err)
        print('修改失败！')
    return redirect(reverse('index'))


def details(request, hid):
    """ 查看远程主机详情 """

    ipaddr = request.GET.get('ip')
    print(ipaddr)
    print("id = %s" % hid)

    ob = Host.objects.get(id=hid)
    print(ob)

    context = {"interval": 5, 'host': ob}
    return render(request, "monitor/details.html", context)


def manual(request):
    return render(request, "monitor/manual.html")


def settings(request):
    return render(request, "monitor/settings.html")


def login(request):
    return render(request, "login.html")


def dologin(request):
    # 校验验证码
    try:
        # 根据账号获取登录者信息
        user = User.objects.get(username=request.POST['username'])

        m = hashlib.md5()
        m.update(bytes(request.POST['password'], encoding="utf8"))
        #print(m.hexdigest())
        if user.password == m.hexdigest():
            # 此处登录成功，将当前登录信息放入到session中，并跳转页面
            request.session['adminuser'] = user.username
            # print(json.dumps(user))
            return redirect(reverse('index'))
        else:
            context = {'info': '登录密码错误！'}
    except Exception as err:
        print(err)
        context = {'info': '登录账号错误！'}
    return render(request, "login.html", context)


def logout(request):
    # 清除登录的session信息
    del request.session['adminuser']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('login'))