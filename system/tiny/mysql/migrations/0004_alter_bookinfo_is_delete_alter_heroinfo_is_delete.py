# Generated by Django 4.1.1 on 2022-10-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysql', '0003_rename_bpub_data_bookinfo_bpub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
    ]