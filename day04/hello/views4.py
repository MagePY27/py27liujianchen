from django.shortcuts import render
from django.views.generic import View, TemplateView
from hello.form import UserForm
from hello.form import UsersForm
import os ##文件上传调用os 模块
import logging

class HtmlView(TemplateView):
    template_name = "hello/1.html"

    def post(self, request):
        print(request.POST)
        ##一键一值
        # data = request.POST.dict()
        # print(data)
        ##一键多值
        # hobby = request.POST.getlist('hobby','')
        # print(hobby)
        ##自定义高效方法（字典生成式）
        # print(dict(request.POST))
        # data1 = dict((k,','.join(v)) for k,v in dict(request.POST).items())
        # print(data1)
        #
        # ##接受文件，并二进制方式读取文件，然后存储
        file = request.FILES.get('file',None)
        print(file)
        print(type(file)) ##by比特类型打印类型
        # ####接收文件并写入
    # def post(self, request):
    #     print(request.POST)
        form  = UserForm(request.POST, request.FILES)
        print("已经进行了表单的验证")
        if form.is_valid():
            print("表单验证OK")
            print(form.cleaned_data)
        if file:
                f = open(os.path.join('upload', file.name),'wb')##wb的意思写入by比特
                for line in file.chunks():
                    f.write(line)
                f.close()

        return render(request,'hello/1.html',{'form':form})
        # return render(request,'hello/1.html')


class FormView(View):
    def get(self, request):
        form = UserForm() #实例化一个表单对象，如果没有提交数据，就显示空表单
        print(form)
        return render(request,'form.html') #空表单在前台显示

    def post(self, request):
        form = UserForm(request.POST) # 将表单数据绑定到form 变量中
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['name']
        return render(request, 'form.html', {'form':form})


class UserModelFormView(View):
    msg = ""

    def get(self, request):
        return render(request,"hello/user_form.html",{"msg":self.msg})

    def post(self, request):
        form = UserModelFormView(request.POST)
        print(form)
        if form.is_valid():
                print(form.cleaned_data)
        return render(request, "hello/user_form.html",{'form':form,"msg":self.msg})



