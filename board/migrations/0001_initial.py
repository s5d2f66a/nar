# Generated by Django 3.2.7 on 2021-11-16 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('photos', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.boardmember', verbose_name='작성자')),
            ],
            options={
                'verbose_name': '게시판',
                'verbose_name_plural': '게시판',
                'db_table': 'posts',
            },
        ),
    ]
