from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.core.paginator import Paginator

from common.models import Users, Types, Goods
from datetime import datetime

# Create your views here.

# 公共信息加载函数
def loadinfo(request):
    lists = Types.objects.filter(pid=0)
    context = {'typelist':lists}
    return context


# =============商品展示========================

def index(request):
    ''' 项目前台首页 '''
    context = loadinfo(request)

    # 获取商品列表中点击量前5作为热销商品（降序排列）
    sellhot = Goods.objects.order_by("-clicknum")[:5]
    print("热销商品")
    num = 0
    for good in sellhot:
        num = num + 1
        print("%02d: %s" %(num, good.goods))

    context['sellhot'] = sellhot
    return render(request, "web/index.html", context)


def lists(request, pIndex=1):
    ''' 商品列表页 '''
    context = loadinfo(request)

    mod = Goods.objects

    # 判断封装搜索条件
    mywhere = []

    tid = int(request.GET.get("tid", 0))
    if tid > 0:
        list = mod.filter(typeid__in=Types.objects.only('id').filter(pid=tid))
        mywhere.append('tid='+str(tid))
    else:
        list = mod.filter()

    # 分页
    pIndex = int(pIndex)
    page = Paginator(list, 8)
    maxpages = page.num_pages
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表

    # 封装模板中需要的信息
    context['goodslist'] = list2
    context['plist'] = plist
    context['pIndex'] = pIndex
    context['mywhere'] = mywhere

    return render(request, "web/list.html", context)


def detail(request, gid):
    ''' 商品详情页 '''
    context = loadinfo(request)

    ob = Goods.objects.get(id=gid)
    ob.clicknum += 1
    ob.save()
    context['goods'] = ob
    return render(request, "web/detail.html", context)


# =============前台验证码========================

def verify(request):
    ''' 生成验证码 '''

    width = 100
    height = 28

    # 导入随机函数模块
    import random, io
    from PIL import Image, ImageDraw, ImageFont

    # 背景颜色
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100),100)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 设置字体
    font = ImageFont.truetype('static/msyh.ttf', 18)
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)

    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 验证码候选值
    bulk = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += bulk[random.randrange(0, len(bulk))]

    # 绘制4个字
    draw.text((5, 0), rand_str[0], font=font, fill=fontcolor)
    draw.text((30, -2), rand_str[1], font=font, fill=fontcolor)
    draw.text((55, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((80, 0), rand_str[3], font=font, fill=fontcolor)

    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str

    # 内存文件操作
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')

    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

# ==============前台会员登录====================

def login(request):
    ''' 会员登录表单 '''
    return render(request,'web/login.html')


def dologin(request):
    ''' 会员执行登录 '''
    # 校验验证码
    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        context = {'info':'验证码错误！'}
        return render(request,"web/login.html",context)

    try:
        #根据账号获取登录者信息
        user = Users.objects.get(username=request.POST['username'])
        #判断当前用户是否是后台管理员用户
        if user.state == 0 or user.state == 1:
            # 验证密码
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'],encoding="utf8"))
            if user.password == m.hexdigest():
                # 此处登录成功，将当前登录信息放入到session中，并跳转页面
                request.session['vipuser'] = user.toDict()
                return redirect(reverse('index'))
            else:
                context = {'info':'登录密码错误！'}
        else:
            context = {'info':'此用户为非法用户！'}
    except:
        context = {'info':'登录账号错误！'}
    return render(request,"web/login.html",context)


def logout(request):
    ''' 会员退出 '''
    # 清除登录的session信息
    del request.session['vipuser']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('login'))


def register(request):
    ''' 会员注册表单 '''
    return render(request,'web/register.html')


def insertUser(request):
    """ 执行添加 """
    try:
        ob = Users()
        ob.username = request.POST['username']
        ob.name = request.POST['name']
        #获取密码并md5
        import hashlib
        m = hashlib.md5()
        m.update(bytes(request.POST['password'],encoding="utf8"))
        ob.password = m.hexdigest()
        ob.sex = 1
        ob.address = ""
        ob.code = ""
        ob.phone = request.POST['phone']
        ob.email = ""
        ob.state = 1
        ob.addtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context={"info":"注册成功，请登录！"}
    except Exception as err:
        print(err)
        context={"info":"注册失败！"}
    return render(request,"web/register.html",context)
