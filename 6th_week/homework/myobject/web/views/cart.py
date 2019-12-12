from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


from common.models import Types,Goods

# 公共信息加载函数
def loadinfo(request):
    lists = Types.objects.filter(pid=0)
    context = {'typelist':lists}
    return context


def index(request):
    ''' 浏览购物车 '''
    context = loadinfo(request)
    if 'shoplist' not in request.session:
    	request.session['shoplist']={}
    return render(request,"web/cart.html",context)


def add(request,gid):
    ''' 添加购物车 '''
    goods = Goods.objects.get(id=gid)
    shop = goods.toDict()
    shop['m'] = int(request.POST.get("m",1))
    shoplist = request.session.get("shoplist",{})
    #判断购物车中是否已存在要购买的商品
    if gid in shoplist:
        shoplist[gid]['m'] += shop['m'] #累加购买量
    else:
        shoplist[gid] = shop
    #将购物车中的商品信息放回到session中
    request.session['shoplist'] = shoplist
    #跳转查看购物车
    return redirect(reverse('cart_index'))


def delete(request,gid):
    ''' 删除购物车中的商品 '''
    shoplist = request.session['shoplist']
    del shoplist[gid]
    request.session['shoplist'] = shoplist
    return redirect(reverse('cart_index'))


def clear(request):
    ''' 清空购物车 '''
    request.session['shoplist'] = {}
    return redirect(reverse('cart_index'))


def change(request):
    ''' 购物车信息修改 '''
    shoplist = request.session['shoplist']
    shopid = request.GET.get("gid",0)
    num = int(request.GET.get('num',1))
    if num < 1:
        num = 1
    shoplist[shopid]['m'] = num
    request.session['shoplist'] = shoplist
    return redirect(reverse('cart_index'))
