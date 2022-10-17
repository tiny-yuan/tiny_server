from datetime import date

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

# 1、查看数据
# BookInfo.objects.all()
# 修改显示信息：在model中修改
# 导入类
from .models import BookInfo, HeroInfo


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

    # 2、 获取单条数据get，不能获取多条数据，不能获取没有的数据，否则会报错，所有使用get需谨慎
    # 可以获取多条,可以没有数据，filter 返回的是列表
    # name = BookInfo.objects.get(id=1) .first() 有值得返回数类表中的第一条数据，没有值得是时候返回None,
    # 但是不会报错
    # name = BookInfo.objects.filter(is_delete=0).first()
    # print(type(name))
    # # name是一个对象
    # print(name.bpub_date)

    # 3、查询数据表中的数据量count()
    # name = BookInfo.objects.count()

    # 4、模糊查找 类似mysql中的like
    # name = BookInfo.objects.filter(btitle__contains='传')
    # 以什么开始：
    # name = BookInfo.objects.filter(btitle__startswith='天')
    # 以什么结束：
    # name = BookInfo.objects.filter(btitle__endswith='湖')

    # 5、空判断：msyql（is /is not）
    # django: isnull
    # name = HeroInfo.objects.filter(hname__isnull=False)

    # 6、范围查询：mysql（in 、between and）
    # django:in
    # name = BookInfo.objects.filter(id__in=[1, 3])
    # 比较查询 gt 大于  lt 小于 gte大于等于 lte 小于等于 等于 = exclude 不等于

    # name = BookInfo.objects.exclude(id=3)
    # 7、查询日期

    # name = BookInfo.objects.filter(bpub_date__year=1995)
    # name = BookInfo.objects.filter(bpub_date__gte = date(1982,1,1))

    # 8、F对象和Q对象
    from django.db.models import F
    from django.db.models import Q
    # mysql:子查询：F查询
    # 查询本条数据阅读量大于评价量
    # name = BookInfo.objects.filter(bread__gt=F("bcomment")/2)

    # Q对象：多个条件查询 逗号就and
    # HeroInfo.objects.filter(id__gt=23, hgender=0)
    # HeroInfo.objects.filter(id__gt=23).filter(hgender=0)

    # 使用Q对象 &表示and |表示or
    # name = BookInfo.objects.filter(Q(id=3) & Q(bread=20))

    # 9、集合函数
    # Avg() 平均，sum()求和 MAX 最大 MIN最小 COUNT计数
    from django.db.models import Avg, Sum, Max, Min, Count
    name = BookInfo.objects.aggregate(Sum("bread"))

    # 10、排序 oder by
    name = BookInfo.objects.all().order_by("bread")  # 正序
    name = BookInfo.objects.all().order_by("-bread")  # 倒序

    # 11、外键搜索（表与表之间）
    # 查询天龙八部中的人物
    b = BookInfo.objects.filter(btitle="天龙八部")[0]
    # 找b中的对的英雄
    # 母表中的对象.HEROINFO 对象 小写_set找到母表中对应的子表.all()
    # print(b.heroinfo_set.all())
    # print(b.heroinfo_set.filter(id=9))

    # 多对一（从子表中找母表）
    # h = HeroInfo.objects.filter(hname="令狐冲")[0]
    # 子表中的字段名
    # b = h.hbook
    # print(b)

    # 增加数据
    # 1、create 直接添加数据
    # BookInfo.objects.create(
    #     btitle="西游记",
    #     bpub_date="1991-01-01",
    #     bread=31,
    #     bcomment=51
    # )
    # 2、save 需要两步
    # b = BookInfo(
    #     btitle="红楼梦",
    #     bpub_date="1922-1-1"
    # )
    # b.save()

    # 修改数据
    # 第一种方法

    # b = BookInfo.objects.filter(id=6)[0] # 1、获取数据
    # b.btitle = "三国演义" # 2、修改数据
    # b.bpub_date = "1911-1-1"
    # b.save() # 3、保存

    # 第二种方法 获取和修改

    # b = BookInfo.objects.filter(id=7)  # 获取数据
    # b.update(
    #     bread=10,
    #     bcomment=15
    # )  # 更新数据 使用的是filter对象

    # 删除

    # b = BookInfo.objects.filter(id=7)  # 获取数据
    # b.delete()  # 删除数据
    #
    # return HttpResponse("数据删除成功！")

    # 模板数据调用


def tmp_mysql(request):
    # 第一种方法
    # hero = HeroInfo.objects.filter(id=3)[0]
    # 三个参数：1、request请求 2、静态文件路径 3、字典类型的数据 前端叫json 长得像字典的字符串
    # 4、网页接受{{键名}}
    # data = {
    #     "hero": hero.hname,
    #     "gender": hero.hgender
    # }
    # redner 渲染数据到前端界面
    # return render(request, "hero.html", data)

    #  第二种方法
    from django.template import loader
    temp = loader.get_template("hero.html")  # 加载html文件
    hero = HeroInfo.objects.filter(id=4)[0]
    data = {
        "hero": hero.hname,
        "gender": hero.hgender
    }
    return render(request, "hero.html", data)


