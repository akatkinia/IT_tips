from django.db import models

# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=255) # max_length позволяет указать длину строки
    content = models.TextField(blank=True) # blank позволяет не задавать значения поля когда создаётся новая запись
    time_create = models.DateTimeField(auto_now_add=True) # auto_now_add автоматически заполняет поле, но только в момент первого появления записи
    time_update = models.DateTimeField(auto_now=True) # auto_now автоматически меняется если меняется текущая запись
    is_published = models.BooleanField(default=True) # default по умолчанию статья будет опубликована

    def __str__(self):
        return self.title