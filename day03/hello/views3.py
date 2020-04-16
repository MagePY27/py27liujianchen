from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import reverse
from django.views.generic import View, TemplateView, ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from hello.models import User
##用户添加
class UserAddView(SuccessMessageMixin, CreateView):

    model = User
    fields = ('name','password','sex')
    success_message  = "%(name)s was created successfully"

    def get_success_url(self):
        print(self.request.POST)
        if  '_addanother' in self.request.POST:
            return reverse('hello:useradd1')
        return reverse('hello:userlist1')
##用户详情
class UserDetailView(DetailView):
    template_name = "hello/user_detail.html"
    model = User
    contest_object_name = "user"
##用户列表
class UserListView(ListView):
    model = User
    context_object_name = "users"
    keyword = ""
#数据过滤
    def get_queryset(self):
        queryset = super(UserListView, self).get_queryset()
        self.keyword = self.request.GET.get("keyword","")
        if self.keyword:
            queryset = queryset.filter(name__contains=self.keyword)
        return queryset
#需要传前端的数据大字典
def get_context_data(self, **kwargs):
    contest= super(UserListView, self).get_context_data(**kwargs)
    contest['keyword']
    return  contest
##用户更新
class UserUpdateView(SuccessMessageMixin,UpdateView):
    template_name = "hello/user_edit.html"
    model = User
    fields = ('name','password','sex')
    success_message = "%(name)s was update successfully"
    def get_success_url(self):
        if '_continue' in self.request.POST:
            return reverse('hello:modify1', kwargs={'pk':self.object.pk})
        return reverse('hello:userlist1')

##用户删除
class UserDeleteView(DeleteView):

    model = User

    def get_success_url(self):
        return reverse('hello:userlist1')






