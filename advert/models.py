from django.db import models

class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание', )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, есть ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta():
        db_table='advertisements'

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

