from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 返回前端数据函数
# request 请求

def test(request):
    return HttpResponse("hello django")

def test1(request):
    return HttpResponse("请说中国话！")