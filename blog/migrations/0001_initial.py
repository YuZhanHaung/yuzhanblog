# Generated by Django 2.2.3 on 2019-07-15 11:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='博客分類')),
            ],
            options={
                'verbose_name': '博客分類',
                'verbose_name_plural': '博客分類',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='博客標籤')),
            ],
            options={
                'verbose_name': '博客標籤',
                'verbose_name_plural': '博客標籤',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='文章標題')),
                ('img', models.ImageField(blank=True, null=True, upload_to='blog_images', verbose_name='博客配圖')),
                ('body', models.TextField(verbose_name='博客正文')),
                ('abstract', models.TextField(blank=True, max_length=256, null=True, verbose_name='博客摘要')),
                ('visiting', models.PositiveIntegerField(default=0, verbose_name='博客訪問量')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='創建時間')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='創建時間')),
                ('author', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL, verbose_name='博客作者')),
                ('category', models.ManyToManyField(to='blog.Category', verbose_name='博客分類')),
                ('tags', models.ManyToManyField(to='blog.Tag', verbose_name='博客標籤')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
                'ordering': ['-created_time'],
            },
        ),
    ]
