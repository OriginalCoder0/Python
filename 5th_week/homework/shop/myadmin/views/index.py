from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from common.models import Users

# Create your views here.


def index(request):
    ''' 后台管理首页 '''
    return render(request, "myadmin/index.html")
    # 要先登录才能进行下去
    #return redirect(reverse('myadmin_login'))


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


def login(request):
    ''' 会员登录表单 '''
    return render(request, 'myadmin/login.html')


def dologin(request):
    ''' 点击后台登录就会跳到这里 '''

    # 校验验证码
    verifycode = request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        context = {'info': '验证码错误！'}
        return render(request, "myadmin/login.html", context)
    try:
        # 根据账号获取登录者信息
        user = Users.objects.get(username=request.POST['username'])
        # 判断当前用户是否是后台管理员用户
        if user.state == 0:
            # 验证密码
            import hashlib
            m = hashlib.md5()
            m.update(bytes(request.POST['password'], encoding="utf8"))
            if user.password == m.hexdigest():
                # 此处登录成功，将当前登录信息放入到session中，并跳转页面
                request.session['adminuser'] = user.name
                # print(json.dumps(user))
                return redirect(reverse('myadmin_index'))
            else:
                context = {'info': '登录密码错误！'}
        else:
            context = {'info': '此用户非后台管理用户！'}
    except Exception as err:
        print(err)
        context = {'info': '登录账号错误！'}
    return render(request, "myadmin/login.html", context)

# 会员退出


def logout(request):
    # 清除登录的session信息
    del request.session['adminuser']
    # 跳转登录页面（url地址改变）
    return redirect(reverse('myadmin_login'))
    # 加载登录页面(url地址不变)
    # return render(request,"myadmin/login.html")
