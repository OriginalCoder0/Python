from django.conf.urls import url

from myadmin.views import index, users, type, goods, orders

urlpatterns = [
    # 后台首页
    url(r'^$', index.index, name="myadmin_index"),

    # 后台管理员路由
    url(r'^login$', index.login, name="myadmin_login"),
    url(r'^dologin$', index.dologin, name="myadmin_dologin"),
    url(r'^logout$', index.logout, name="myadmin_logout"),
    url(r'^verify$', index.verify, name="myadmin_verify"), #验证码

    # 会员信息管理路由
    url(r'^users/(?P<pIndex>[0-9]+)$', users.index, name="myadmin_users_index"),
    url(r'^users/add$', users.add, name="myadmin_users_add"),
    url(r'^users/insert$', users.insert, name="myadmin_users_insert"),
    url(r'^users/del/(?P<uid>[0-9]+)$', users.delete, name="myadmin_users_del"),
    url(r'^users/edit/(?P<uid>[0-9]+)$', users.edit, name="myadmin_users_edit"),
    url(r'^users/update/(?P<uid>[0-9]+)$', users.update, name="myadmin_users_update"),
    url(r'^users/resetpass/(?P<uid>[0-9]+)$', users.resetpass, name="myadmin_users_resetpass"),
    url(r'^users/doresetpass/(?P<uid>[0-9]+)$', users.doresetpass, name="myadmin_users_doresetpass"),

     # 商品类别信息管理路由
    url(r'^type$', type.index, name="myadmin_type_index"),
    url(r'^type/add/(?P<tid>[0-9]+)$', type.add, name="myadmin_type_add"),
    url(r'^type/insert$', type.insert, name="myadmin_type_insert"),
    url(r'^type/del/(?P<tid>[0-9]+)$', type.delete, name="myadmin_type_del"),
    url(r'^type/edit/(?P<tid>[0-9]+)$', type.edit, name="myadmin_type_edit"),
    url(r'^type/update/(?P<tid>[0-9]+)$', type.update, name="myadmin_type_update"),

    # 商品信息管理路由
    url(r'^goods/(?P<pIndex>[0-9]+)$', goods.index, name="myadmin_goods_index"),
    url(r'^goods/add$', goods.add, name="myadmin_goods_add"),
    url(r'^goods/insert$', goods.insert, name="myadmin_goods_insert"),
    url(r'^goods/del/(?P<gid>[0-9]+)$', goods.delete, name="myadmin_goods_del"),
    url(r'^goods/edit/(?P<gid>[0-9]+)$', goods.edit, name="myadmin_goods_edit"),
    url(r'^goods/update/(?P<gid>[0-9]+)$', goods.update, name="myadmin_goods_update"),

    # 订单信息管理路由
    url(r'^orders$', orders.index, name="myadmin_orders_index"),
    url(r'^orders/(?P<pIndex>[0-9]+)$', orders.index, name="myadmin_orders_index"),
    url(r'^orders/detail/(?P<oid>[0-9]+)$', orders.detail, name="myadmin_orders_detail"),
    url(r'^orders/state$',orders.state, name="myadmin_orders_state"),
]
