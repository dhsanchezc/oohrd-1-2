from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20, verbose_name='Nombre')
    address=models.CharField(max_length=30, verbose_name='Dirección')
    email=models.CharField(max_length=30, verbose_name='Correo')
    favorite_food=models.CharField(max_length=50, verbose_name='Comida favorita')