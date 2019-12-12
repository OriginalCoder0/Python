from django.shortcuts import redirect
from django.core.urlresolvers import reverse

import re

class ShopMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        print("ShopMiddleware")

    def __call__(self, request):
        # 定义网站后台不用登录也可访问的路由url
        urllist = ['/myadmin/login','/myadmin/dologin','/myadmin/logout','/myadmin/verify']
        # 获取当前请求路径
        path = request.path
        print("mycall..."+path)
        # 判断当前请求是否是访问网站后台,并且path不在urllist中
        if re.match("/myadmin",path) and (path not in urllist):
            # 判断当前用户是否没有登录
            if "adminuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('myadmin_login'))

        # 网站前台登录用户判断（订单操作和会员中心操作需登录）
        if re.match("^/orders", path) or re.match("^/vip", path):
            # 判断当前用户是否没有登录
            if "vipuser" not in request.session:
                # 执行登录界面跳转
                return redirect(reverse('login'))
        
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response