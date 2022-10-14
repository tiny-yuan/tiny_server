import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
# 重定向库
from django.shortcuts import redirect
# HttpResponse 返回的数据是字符串
# JsonResponse 返回的数据是字典

# Create your views here.
def weather(request,city,year):
    print(city)
    print(year)
    # 快捷导入 alt+enter
    return HttpResponse("ok")
def live(request,city,year):
    print(city)
    print(year)
    # 快捷导入 alt+enter
    return HttpResponse("ok")

def tiny(request):
    city = request.GET.get("city")
    year = request.GET.get("year")
    print(city)
    print(year)
    return HttpResponse("ok")

def request_body(request):
    city = request.POST.get("city")
    year = request.POST.get("year")
    print(city)
    print(year)

    return HttpResponse("ok")

def json_body(request):
    json_data = request.body
    # print(json_data)
    # 转成字符串
    json_str = json_data.decode()
    print(json_str,type(json_str))
    # 转成字典
    json_dict = json.loads(json_str)
    print(json_dict,type(json_dict))
    # 获取city
    city = json_dict["city"]
    # 获取年份
    year = json_dict["year"]
    print(city)
    print(year)
    return HttpResponse("ok")

def request_header(request):
    data = request.META["CONTENT_TYPE"]
    print(data)
    city = request.POST.get("city")
    year = request.POST.get("year")
    print(city)
    print(year)
    return HttpResponse("ok")

# 相应对象
def response_obj(request):
    # data = '{"name": "李大爷"}'
    # response = HttpResponse(data, content_type="application/json", status=200)
    # response["content"] = "@tiny"
    # response["new_name"] = "liyuan"
    data = {'name': '大爷'}
    # 500编码服务器错误
    return JsonResponse(data)
# 重定向 重新定义显示函数
def red(request):
    # return HttpResponse("显示red")
    # return redirect("/static/0.jpg")
    return redirect("/api/res/")
def res(request):
    return HttpResponse("显示res")

# cookie:名称 内容 name:value
# cookie信息：（浏览临时会话时结束） 保存在浏览器上
# 浏览器（客户端） 》》 服务器（数据库） 默认15天清楚cookie信息 商场网站清楚cookie信息一般时间为一个小时
def do_cookie(request):
    # 响应体
    response = HttpResponse("传递cookie")
    # 设置cookie响应头
    # response.set_cookie("name", "lidaye")
    # 设置时效cookie 单位是秒
    response.set_cookie("name", "lidaye", max_age=10)
    return response
def cat_cookie(request):
    cookie = request.COOKIES.get("name")
    if cookie:
        return HttpResponse("获取到cookie，值是：%s" %cookie)
    else:
        return HttpResponse("无效cookie")

# session：保存在服务器上

# 设置session

def set_session(request):
    request.session["user_id"] = 100
    request.session["user_name"] = "lidaye"
    # 设置过期时间 单位是s
    # request.session.set_expiry(30)

    # 删除数据

    # 整条删除
    # request.session.flush()
    # 删除某个值
    del request.session["user_id"]
    return HttpResponse("session设置成功")
# 获取session
def get_session(request):
    user_id = request.session.get("user_id")
    user_name = request.session.get("user_name")
    if user_name:
        return HttpResponse("redis数据库中存的session值:user_id={},user_name={}".format(user_id,user_name))
    else:
        return HttpResponse("session无效")
