# Generated by Django 3.2.7 on 2021-09-10 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text_of_article',
            field=models.TextField(default='В процессе написания...', help_text='Введите текст статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='Введите название статьи', max_length=100),
        ),
    ]
