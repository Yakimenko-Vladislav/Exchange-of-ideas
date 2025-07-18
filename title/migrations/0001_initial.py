# Generated by Django 4.0.4 on 2022-05-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moniker', models.CharField(max_length=100, verbose_name='Название идеи')),
                ('content', models.TextField(verbose_name='Описание идеи')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('author', models.CharField(blank=True, max_length=50, null=True, verbose_name='Автор')),
                ('password', models.CharField(blank=True, max_length=50, null=True, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Идея',
                'verbose_name_plural': 'Идеи',
            },
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('nickname', models.CharField(max_length=100, verbose_name='Название идеи')),
                ('appraising', models.IntegerField(verbose_name='Оценка пользователем')),
            ],
            options={
                'verbose_name': 'Критик',
                'verbose_name_plural': 'Критики',
            },
        ),
    ]
