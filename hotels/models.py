from django.db import models
from django.core.validators import validate_email
from phonenumber_field.modelfields import PhoneNumberField


class City(models.Model):
    name = models.CharField("Название города", max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(verbose_name="Название отеля", max_length=255, null=False, blank=False)
    address = models.TextField(verbose_name='Адрес отеля', null=False, blank=True)
    contact_email = models.CharField(verbose_name='Контактный email', max_length=255, blank=True, null=True,
                                     validators=[validate_email])
    city = models.ForeignKey(City, verbose_name="Город", related_name="cities", on_delete=models.SET_NULL,
                             blank=True, null=True)
    contact_phone = PhoneNumberField(verbose_name="Контактный номер", null=True, blank=True)

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'

    def __str__(self):
        return f'{self.name} (г.{self.city.name})'
