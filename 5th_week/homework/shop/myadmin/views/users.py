from django.shortcuts import render
from common.models import Users
from datetime import datetime
from django.core.paginator import Paginator


def index(request, pIndex):
    ''' 浏览会员信息 '''

    # 获取商品类别信息
    list = Users.objects.all()

    # 获取商品信息查询对象
    mod = Users.objects
    mywhere = []  # 定义一个用于存放搜索条件列表

    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("keyword", None)
    if kw:
        # 查询商品名中只要含有关键字的都可以
        list = mod.filter(username__contains=kw)
        mywhere.append("keyword=" + kw)
    else:
        list = mod.filter()
    # 获取、判断并封装性别sex搜索条件
    sex = request.GET.get('sex', '')
    if sex != '':
        list = list.filter(sex=sex)
        mywhere.append("sex=" + sex)

    # 执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list, 5)  # 以5条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表

    # 封装信息加载模板输出
    context = {"userslist": list2, 'plist': plist, 'pIndex': pIndex,
               'maxpages': maxpages, 'mywhere': mywhere}
    return render(request, "myadmin/users/index.html", context)


def add(request):
    ''' 会员信息添加表单 '''
    return render(request, 'myadmin/users/add.html')


def insert(request):
    ''' 执行会员信息添加 '''
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        # 获取密码并md5
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'], encoding="utf8"))
        ob.password = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info': '添加成功！'}
    except Exception as err:
        print(err)
        context = {'info': '添加失败！'}

    return render(request, "myadmin/info.html", context)


def delete(request, uid):
    ''' 执行会员信息删除 '''
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {'info': '删除成功！'}
    except Exception as err:
        print(err)
        context = {'info': '删除失败！'}
    return render(request, "myadmin/info.html", context)


def edit(request, uid):
    ''' 打开会员信息编辑表单 '''
    try:
        ob = Users.objects.get(id=uid)
        context = {'user': ob}
        return render(request, "myadmin/users/edit.html", context)
    except Exception as err:
        print(err)
        context = {'info': '没有找到要修改的信息！'}
    return render(request, "myadmin/info.html", context)


def update(request, uid):
    ''' 执行会员信息编辑 '''
    try:
        ob = Users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = request.POST['state']
        ob.save()
        context = {'info': '修改成功！'}
    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}
    return render(request, "myadmin/info.html", context)


def resetpass(request, uid):
    ''' 打开会员信息编辑表单 '''
    try:
        ob = Users.objects.get(id=uid)
        context = {'user': ob}
        return render(request, "myadmin/users/resetpass.html", context)
    except Exception as err:
        print(err)
        context = {'info': '没有找到要修改的信息！'}
    return render(request, "myadmin/info.html", context)


def doresetpass(request, uid):
    ''' 执行会员信息编辑 '''
    try:
        ob = Users.objects.get(id=uid)
        # 获取密码并md5
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'], encoding="utf8"))
        ob.password = m.hexdigest()
        ob.save()
        context = {'info': '修改成功！'}
    except Exception as err:
        print(err)
        context = {'info': '修改失败！'}
    return render(request, "myadmin/info.html", context)
