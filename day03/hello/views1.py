from django.http import HttpResponse,QueryDict
from django.shortcuts import render
from  hello.models import User
from django.template import loader,Context,RequestContext
from django.shortcuts import get_object_or_404
from django.http import Http404
import traceback
# 增加
def useradd(request):
    msg = {}
    if request.method == "POST":
        try:
             print (request.POST)
             # name = request.POST.get('name',"")
             # password = request.POST.get('password',"")
             # sex = request.POST.get('sex',"")
             # print(name)
             # u = User()
             # u.name = name
             # u.password = password
             # u.sex = int(sex)
             # u.save()
             data = request.POST.dict()
             print(data)
             User.objects.create(**data)
             msg = {"code": 0, "result": "添加用户成功"}
        except:
             msg = {"code": 1, "errmsg": "添加用户失败: %s" % traceback.format_exc()}
    return render(request,"hello/useradd.html",{"msg":msg})

# 查看
def userlist(request):

    keyword = request.GET.get("keyword","")
    print(keyword)
    users = User.objects.all()
    if keyword:
        users = users.filter(name__contains=keyword) ##数据库模糊查询
    print(users)
    return render(request,'hello/userlist.html',{"users":users,"keyword":keyword})
# 更新
def modify(request, **kwargs):
    msg = {}
    print(kwargs)
    pk = kwargs.get("pk")
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        try:
            data = request.POST.dict()
            print(data)
            User.objects.filter(pk=pk).update(**data)
            msg = {"code": 0, "result": "更新用户成功"}
        except:
            msg = {"code":1, "errmsg":"更新用户失败: %s" % traceback.format_exc()}
    return render(request,"hello/modify.html",{"user":user, "msg":msg})

# 删除
def userdel(request, **kwargs):
    msg = {}
    pk = kwargs.get("pk")
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404

    if request.method == "POST":
        try:
            User.objects.get(pk=pk).delete()
            msg = {"code":0, "result":"删除用户成功"}
        except:
            msg = {"code":1, "errmsg":"删除用户失败 %s" % traceback.format_exc()}
    return  render(request,"hello/userdel.html",{"user":user,"msg":msg})