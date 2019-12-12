from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Photos
from PIL import Image
import time, os
from django.core.paginator import Paginator

# Create your views here.

def index(request):
	""" 在线相册首页 """
	return render(request, "myapp/index.html")


def indexPhotos(request, pIndex):
	""" 在线相册浏览页面 """
	# 获取所有图片信息
	list = Photos.objects.all()

	# 分页
	p = Paginator(list, 6)
	if pIndex == "":
		pIndex = "1"
	aList = p.page(pIndex)
	pList = p.page_range
	context = {"photoslist": aList, "pList": pList, "pIndex": int(pIndex)}

	# 将信息封装到字典中
	#context = {"photoslist":list}
	# 加载模板，并传递信息
	return render(request, "myapp/photos/index.html", context)


def addPhotos(request):
	""" 添加图片页面 """
	return render(request, "myapp/photos/add.html")


def insertPhotos(request):
	""" 将添加的图片信息更新到数据库 """
	try:
		ob = Photos()
		print("get photo")
		ob.title = request.POST['title']
		ob.comment = request.POST['comment']
		#ob.filename = request.POST['pic']

		img = request.FILES.get("img", None)
		if not img:
			return HttpResponse("Nothing uploaded")
		fileName = str(time.time()) + "." + img.name.split('.').pop()
		destination = open("./static/pics/" + fileName, "wb+")
		for chunk in img.chunks():
			destination.write(chunk)
		destination.close()

		# Save image file name to DB
		ob.filename = fileName

		# Resize the image
		im = Image.open("./static/pics/" + fileName)
		im.thumbnail((64, 64))
		im.save("./static/pics/s_" + fileName, None)

		ob.save()
		print('Save Okay!!!')
		context = {'info':'添加成功！'}
	except:
		context = {'info': '添加失败！'}
	return render(request, "myapp/photos/info.html", context)


def deletePhotos(request, uid):
	""" 删除选择的图片信息，同时删除对应的图片 """
	try:
		ob = Photos.objects.get(id=uid)
		ob.delete()
		os.remove("./static/pics/" + ob.filename)
		os.remove("./static/pics/s_" + ob.filename)
		context = {'info': '删除成功！'}
	except:
		context = {'info': '删除失败！'}
	return render(request, "myapp/photos/info.html", context)


def editPhotos(request, uid):
	""" 修改前准备工作 """
	try:
		ob = Photos.objects.get(id=uid)
		context = {'photo': ob}
		return render(request, "myapp/photos/edit.html", context)
	except:
		context = {'info': '没有找到要修改的信息！'}
		return render(request, "myapp/photos/info.html", context)


def updatePhotos(request):
	""" 将修改更新到数据库 """
	try:
		ob = Photos.objects.get(id=request.POST['id'])
		ob.title = request.POST['title']
		ob.comment = request.POST['comment']

		img = request.FILES.get('img', None)
		print(img)
		if not img:
			ob.filename = request.POST['filename']
		else:
			fileName = str(time.time()) + "." + img.name.split('.').pop()
			destination = open("./static/pics/" + fileName, "wb+")
			for chunk in img.chunks():
				destination.write(chunk)
			destination.close()
			ob.filename = fileName

			# Resize the image
			im = Image.open("./static/pics/" + fileName)
			im.thumbnail((64, 64))
			im.save("./static/pics/s_" + fileName, None)

		ob.save()
		context = {'info':'修改成功！'}
	except:
		context = {'info': '修改失败！'}
	return render(request, "myapp/photos/info.html", context)

