from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


class Account(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome')
    tel = models.CharField(max_length=11, verbose_name='Telefone', unique=True, blank=True)
    dt_nasc = models.DateField(verbose_name='Data de nascimento', blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'



# class Points(models.Model):
#     point_1 = models.BooleanField()
#     point_2 = models.BooleanField()
#     point_3 = models.BooleanField()
#     point_4 = models.BooleanField()
#     point_5 = models.BooleanField()
#     point_6 = models.BooleanField()
#     point_7 = models.BooleanField()
#     point_8 = models.BooleanField()
#     point_9 = models.BooleanField()
#     point_10 = models.BooleanField()
#     usuario = models.ForeignKey(User, on_delete=models.PROTECT)
#
#     def __str__(self):
#         return self.usuario
#
#     class Meta:
#         verbose_name = 'Point'
#         verbose_name_plural = 'Points'
