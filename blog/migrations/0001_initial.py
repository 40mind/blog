# Generated by Django 3.2.7 on 2021-09-10 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text='Введите никнейм', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название статьи', max_length=50)),
                ('date_of_writing', models.DateField(help_text='Выберите дату написания')),
                ('description', models.CharField(help_text='Введите описание', max_length=300)),
                ('author', models.ForeignKey(help_text='Выберите автора', null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.author')),
            ],
        ),
    ]
