from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField('Имя пользователя', max_length=128)
    username = models.CharField('Ник', max_length=128)
    email = models.EmailField('Почта')
    address = models.TextField('Адрес')
    phone = models.CharField('Почта', max_length=128)
    website = models.CharField('Сайт', max_length=128)
    company = models.TextField('Компания')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название статьи', max_length=128)
    body = models.TextField('Текст статьи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
