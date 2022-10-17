from django.db import models

# Create your models here.
# orm中o式object类 ，
# 创建表
# id:django 帮我们自动创建id
class BookInfo(models.Model):
    # 字段
    # CharField：字符串；max_length：字符最大长度；verbose_name：描述信息admin显示 站点管理django后台
    btitle = models.CharField(max_length=30, verbose_name="名称")
    # DateField：1988-0-01
    bpub_date = models.DateField(verbose_name="发布日期")
    # IntegerField：数字（int）2的11次方
    bread = models.IntegerField(default=0, verbose_name="阅读量")
    bcomment = models.IntegerField(default=0, verbose_name="评论量")
    # BooleanField：布尔
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    # 表名
    class Meta:
        # 数据表名
        db_table = "bookinfo"
        verbose_name = "图书"
        # "显示复数 breads"
        verbose_name_plural = verbose_name

    # 修改显示
    # 默认显示id，我想显示名字
    def __str__(self):
        return self.btitle


# 载创建一个表
class HeroInfo(models.Model):
    # menu:(男，女)
    # 先见一个选择变量
    GENER_CHOICES = (
        (0,"male"),   # 0 表示男的
        (1, "female"),  # 1 表示女的

    )
    hname = models.CharField(max_length=20, verbose_name="名称")
    # SmallIntegerField:小整形（0,1）
    hgender = models.SmallIntegerField(choices=GENER_CHOICES, default=0, verbose_name="性别")
    # null: 允许为空 不写就是不允许为空
    hcomment = models.CharField(max_length=200, null=True, verbose_name="描述信息")
    # ForeignKey 外键：1、先有目标，再有子表，母表可以对应很多子表，母表还有关联，就不能删除母表的数据
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name="图书")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    # 表名
    class Meta:
        # 数据表名
        db_table = "heroinfo"
        verbose_name = "英雄"
        # "显示复数 breads"
        verbose_name_plural = verbose_name
    # 修改显示
    # 默认显示id，我想显示名字
    def __str__(self):
        return self.hname