# Generated by Django 3.1.6 on 2021-06-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
