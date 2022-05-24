from django.db import models


class Idea(models.Model):
    moniker = models.CharField('Название идеи', max_length=100)
    content = models.TextField('Описание идеи')
    rating = models.IntegerField('Рейтинг', default=0)
    author = models.CharField('Автор', max_length=50, null=True, blank=True)
    password = models.CharField('Пароль', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.moniker

    class Meta:
        verbose_name = 'Идея'
        verbose_name_plural = 'Идеи'


class Reviewer(models.Model):
    ip = models.GenericIPAddressField('IP адрес')
    nickname = models.CharField('Название идеи', max_length=100)
    appraising = models.IntegerField('Оценка пользователем')

    def __str__(self):
        return str(self.ip) + '; ' + str(self.nickname)

    class Meta:
        verbose_name = 'Критик'
        verbose_name_plural = 'Критики'