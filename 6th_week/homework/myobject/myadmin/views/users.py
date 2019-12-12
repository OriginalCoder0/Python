from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime

from common.models import Users
# Create your views here.
def index(request,pIndex=1):
    '''浏览信息'''
    umod = Users.objects
    mywhere=[]

    # 获取、判断并封装关keyword键搜索
    kw = request.GET.get("keyword",None)
    if kw:
        # 查询账户或真实姓名中只要含有关键字的都可以
        list = umod.filter(Q(username__contains=kw) | Q(name__contains=kw))
        mywhere.append("keyword="+kw)
    else:
        list = umod.filter()
    # 获取、判断并封装性别sex搜索条件
    sex = request.GET.get('sex','')
    if sex != '':
        list = list.filter(sex=sex)
        mywhere.append("sex="+sex)

    #执行分页处理
    pIndex = int(pIndex)
    page = Paginator(list,5) #以5条每页创建分页对象
    maxpages = page.num_pages #最大页数
    #判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex) #当前页数据
    plist = page.page_range   #页码数列表
    

    #封装信息加载模板输出
    context = {"userslist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'mywhere':mywhere}
    return render(request,"myadmin/users/index.html",context)

def add(request):
    '''加载添加页面'''
    return render(request,"myadmin/users/add.html")

def insert(request):
    '''执行添加'''
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        #获取密码并md5
        import hashlib
        m = hashlib.md5() 
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.sex = request.POST['sex']
        ob.address = request.POST['address']
        ob.code = request.POST['code']
        ob.phone = request.POST['phone']
        ob.email = request.POST['email']
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context={"info":"添加成功！"}
    except Exception as err:
        print(err)
        context={"info":"添加失败"}
    return render(request,"myadmin/info.html",context)

def delete(request,uid):
    '''删除信息'''
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context={"info":"删除成功！"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return render(request,"myadmin/info.html",context)


def edit(request,uid):
    '''加载编辑信息页面'''
    try:
        ob = Users.objects.get(id=uid)
        context={"user":ob}
        return render(request,"myadmin/users/edit.html",context)
    except Exception as err:
        context={"info":"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)

def update(request,uid):
    '''执行编辑信息'''
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
        context={"info":"修改成功！"}
    except Exception as err:
        print(err)
        context={"info":"修改失败"}
    return render(request,"myadmin/info.html",context)

def resetpass(request,uid):
    '''加载重置会员密码信息页面'''
    try:
        ob = Users.objects.get(id=uid)
        context={"user":ob}
        return render(request,"myadmin/users/resetpass.html",context)
    except Exception as err:
        context={"info":"没有找到要修改的信息！"}
        return render(request,"myadmin/info.html",context)

def doresetpass(request,uid):
    '''执行编辑信息'''
    try:
        ob = Users.objects.get(id=uid)
        #获取密码并md5
        import hashlib
        m = hashlib.md5() 
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.save()
        context={"info":"密码重置成功！"}
    except Exception as err:
        print(err)
        context={"info":"密码重置失败"}
    return render(request,"myadmin/info.html",context)