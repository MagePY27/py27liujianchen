from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from  hello.models import User
import traceback

def useradd(request):
    msg = {}
    if request.method == "POST":
         try:
             print (request.POST)
             name = request.POST.get('name',"")
             password = request.POST.get('password',"")
             sex = request.POST.get('sex',"")
             print(name)
             u = User()
             u.name = name
             u.password = password
             u.sex = int(sex)
             u.save()
             msg = {"code": 0, "result": "添加用户成功"}
         except:
             msg = {"code": 1, "errmsg": "添加用户失败: %s" % traceback.format_exc()}
    return render(request,'hello/useradd.html',{"msg":msg})
