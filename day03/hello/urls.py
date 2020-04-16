"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from django.urls import re_path
from hello import views
from hello import views1
from hello import views3
from hello import views4
app_name= 'hello'
urlpatterns = [
 #fbv
 # path('useradd/', views1.useradd, name='useradd'),
 # path('userlist/', views1.userlist, name='userlist'),
 # re_path('modify/(?P<pk>[0-9]+)?/',views1.modify,name="modify"),
 # re_path('userdel/(?P<pk>[0-9]+)?/',views1.userdel,name="userdel"),
 # path('html/', views4.HtmlView.as_view(), name="html"),
 #cbv类视图url规则
 path('useradd1/', views3.UserAddView.as_view(), name='useradd1'),
 path('userlist1/', views3.UserListView.as_view(), name='userlist1'),
 re_path('detai1/(?P<pk>[0-9]+)?/',views3.UserDetailView.as_view(),name="detai1"),
 re_path('modify1/(?P<pk>[0-9]+)?/',views3.UserUpdateView.as_view(),name="modify1"),
 re_path('userdel1/(?P<pk>[0-9]+)?/',views3.UserDeleteView.as_view(),name="userdel1"),
]