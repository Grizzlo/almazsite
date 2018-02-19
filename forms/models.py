from __future__ import unicode_literals
from django.utils.translation import gettext_lazy as _t

from django.db import models

HOTEL_CHOICES= [
    ('Алмаз', _t('Алмаз')),
    ('Алмаз-плюс', _t('Алмаз-плюс')),
    ]
CLASSROOM_CHOICES= [
    ('Стандарт', _t('Стандарт')),
    ('Напівлюкс', _t('Напівлюкс')),
    ('Люкс', _t('Люкс')),
    ('Ліжкомісце',_t('Ліжкомісце'))
    ]
TOUR_CHOICES = [
    ('Полтава історична', _t('Полтава історична')),
    ('Етнографічний маршрут “Білим по білому”', _t('Етнографічний маршрут “Білим по білому”')),
    ('Історичне Поле Полтавської битви', _t('Історичне Поле Полтавської битви')),
    ('Літературна Полтава', _t('Літературна Полтава')),
    ('Диканька. Подорож на батьківщину Рудого Панька', _t('Диканька. Подорож на батьківщину Рудого Панька')),
    ('Гоголем оспівана земля!', _t('Гоголем оспівана земля!')),
    ('Історико-культурна спадщина монастирів Полтавщини', _t('Історико-культурна спадщина монастирів Полтавщини')),
    ('Храми Полтави', _t('Храми Полтави')),
    ('Дорогами Сковороди', _t('Дорогами Сковороди')),
    ('Опішне – гончарна столиця України', _t('Опішне – гончарна столиця України')),
    ('Більське городище', _t('Більське городище')),
    ('Миргород. Подорож до королеви мінеральних вод', _t('Миргород. Подорож до королеви мінеральних вод')),
]
# Create your models here.

class BookingModel(models.Model):
        class Meta:
            db_table = "book_room"
            verbose_name = "Бронювання готелю"

        username = models.CharField( verbose_name="ПІБ",max_length = 50)
        tel_user_phone = models.CharField(verbose_name="Телефон",max_length = 30)
        user_email = models.EmailField(verbose_name="Пошта",max_length=255)
        user_comment = models.TextField(verbose_name="Додатковий коментар",blank=True)
        hotel =  models.CharField(verbose_name="Назва Готелю",max_length = 100,choices=HOTEL_CHOICES)
        room_class =  models.CharField(verbose_name="Клас кімнати",max_length = 100,choices=CLASSROOM_CHOICES)
        date_entry = models.CharField(verbose_name="Дата заїзду",max_length = 30)
        date_out = models.CharField(verbose_name="Дата виїзду",max_length = 30)
        number_of_people = models.IntegerField(verbose_name="Кількість людей")
        time = models.TimeField(verbose_name="Час бронювання",auto_now=True)

        def __str__(self):
            return self.username

class BookingTourModel(models.Model):
        class Meta:
            db_table = "book_tour"
            verbose_name = "Бронювання туру"

        username =  models.CharField( verbose_name="ПІБ",max_length = 50)
        tel_user_phone = models.CharField(verbose_name="Телефон",max_length = 30)
        user_email =models.EmailField(verbose_name="Пошта",max_length=255)
        user_comment =models.TextField(verbose_name="Додатковий коментар",blank=True)
        tour_name =  models.CharField(verbose_name="Назва Туру",max_length = 100, choices=TOUR_CHOICES)
        date_entry = models.CharField(verbose_name="Дата виїзду",max_length = 30)
        number_of_people = models.IntegerField(verbose_name="Кількість людей")
        time = models.TimeField(verbose_name="Час бронювання",auto_now=True)

        def __str__(self):
            return self.username
