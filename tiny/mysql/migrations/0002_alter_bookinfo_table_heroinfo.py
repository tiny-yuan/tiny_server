# Generated by Django 4.1.1 on 2022-10-04 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysql', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='bookinfo',
            table='bookinfo',
        ),
        migrations.CreateModel(
            name='Heroinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=20, verbose_name='名称')),
                ('hgender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别')),
                ('hcomment', models.CharField(max_length=200, null=True, verbose_name='描述信息')),
                ('is_delete', models.BooleanField(default=False, verbose_name='路基删除')),
                ('hbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysql.bookinfo', verbose_name='图书')),
            ],
            options={
                'verbose_name': '英雄',
                'verbose_name_plural': '英雄',
                'db_table': 'heroinfo',
            },
        ),
    ]
