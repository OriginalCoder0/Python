from django.conf.urls import url
from . import views

urlpatterns = [
	# 首页
	url(r'^$', views.index, name="index"),

	# 相册浏览
	url(r'^photos/(?P<pIndex>[0-99]+)$', views.indexPhotos, name="photos"),
	# 添加图片信息
	url(r'^photos/add$', views.addPhotos, name="addphotos"),
	url(r'^photos/insert$', views.insertPhotos, name="insertphotos"),
	# 删除图片信息
	url(r'^photos/delete/(?P<uid>[0-9]+)$', views.deletePhotos, name="deletephotos"),
	# 修改图片信息
	url(r'^photos/edit/(?P<uid>[0-9]+)$', views.editPhotos, name="editphotos"),
	url(r'^photos/update$', views.updatePhotos, name="updatephotos"),

]