# Generated by Django 4.1.1 on 2022-10-04 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysql', '0002_alter_bookinfo_table_heroinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='bpub_data',
            new_name='bpub_date',
        ),
    ]
