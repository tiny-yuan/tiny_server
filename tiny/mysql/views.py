from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse("ok")
# 安装mysql和python交互的第三方库
# 在django中配置
# 1、在源文件__init__.py中配置
# 2、在setting中配置
# 3、pycharm中配置图形化显示界面
# 4、语法django操作mysql 除了不能操作数据库，其他都可以（建表、增删改查）

# HTML>django>mysql

# 5、实现数据库迁移：
# 5.1 本地生成数据表：python manage.py makemigrations
# mysqlclient 1.4.0 or newer is required ;you have 0.10.1 改源文件 注销 base.py 中if version...
# 5.2 将本地表迁移到数据库中：python manage.py migrate

# 启动shell python manage.py shell
# 语法连接
# 导入需要的类
# from mysql.models import BookInfo,HeroInfo
# 操作语法

# 查看数据
# BookInfo.objects.all()
# 修改显示信息：在model中修改
# 导入类
from .models import BookInfo,HeroInfo

def do_model(request):
#     book_obj = BookInfo.objects.all()
#     hero_obj = HeroInfo.objects.all()
#     # print(book_obj)
#     name = ""
#     hname = ""
#     for book in book_obj:
# # HeroInfo.objects.all()
#
#         # 获取字段
#         name += book.btitle
#     for hero in hero_obj:
#         # 获取字段
#         hname += hero.hname


    # 获取单条数据get，不能获取多条数据，不能获取没有的数据，否则会报错，所有使用get需谨慎
    # 可以获取多条,可以没有数据，filter 返回的是列表
    # name = BookInfo.objects.get(id=1) .first() 有值得返回数类表中的第一条数据，没有值得是时候返回None,
    # 但是不会报错
    # name = BookInfo.objects.filter(is_delete=0).first()
    # print(type(name))
    # # name是一个对象
    # print(name.bpub_date)


    # 查询数据表中的数据量count()
    # name = BookInfo.objects.count()

    # 模糊查找 类似mysql中的like
    # name = BookInfo.objects.filter(btitle__contains='传')
    # 以什么开始：
    # name = BookInfo.objects.filter(btitle__startswith='天')
    # 以什么结束：
    name = BookInfo.objects.filter(btitle__endswith='湖')
    print(name)
    return HttpResponse("ok书名：{} 英雄名：".format(name))
