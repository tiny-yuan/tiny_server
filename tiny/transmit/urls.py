"""tiny URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import re_path
urlpatterns = [
    # 1.从路径中提取需要的数据 正则提取(城市、年份)
    re_path(r'^weather/([a-zA-Z]+)/(\d{4}/$)', views.weather),
    # 限制符提取数据
    path(r"live/<str:city>/<int:year>/",views.live),

    # 2.类似于键值对的方式提取
    # get方式传递数据
    path("tiny/", views.tiny),

    # 3.请求体传值
    path("request_body/", views.request_body),

    # json传值
    path("json/", views.json_body),

    # 4.请求头  post：传值 安全 数据量大  get传值 快 数据量有限 浏览器专用
    path("request_header/", views.request_header),

    # 响应对象
    path("response_obj/", views.response_obj),
    # 重定向
    path("red/", views.red),
    path("res/", views.res),

    # 设置cookie
    path("do_cookie/", views.do_cookie),
    # 获取cookie
    path("cat_cookie/", views.cat_cookie),

    # 设置session
    path("set_sesssion/", views.set_session),

    # 获取session
    path("get_sesssion/", views.get_session)

]
