from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.html import format_html

User=get_user_model()
class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание', )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, есть ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image=models.ImageField('Изображение', upload_to='Django_prodjango/')

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date()==timezone.now().date():
            created_time=self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; '
                               'font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    @admin.display(description='Дата обновления')
    def updated_date(self):
        if self.updated_at.date()==timezone.now().date():
            updated_time=self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: purple; '
                               'font-weight: bold;">Сегодня в {}</span>', updated_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Фото')
    def photo_method(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 60px; max-height: 150px;"', url=self.image.url)



    class Meta():
        db_table='advertisements'

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

