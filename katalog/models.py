from django.db import models
from django.urls import reverse


class Company(models.Model):
    '''Таблиця компанії'''
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TypePuzzle(models.Model):
    '''Таблиця типу'''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Puzzle(models.Model):
    '''Таблиця товару'''
    type = models.ForeignKey(TypePuzzle, on_delete=models.CASCADE, null=True, default='3')
    model = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, default='1')
    img = models.ImageField(blank=True, upload_to='puzzles/img/%Y/%m/%d')
    price = models.IntegerField(blank=True, default=100)
    counter = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.model}'

    def get_url(self):
        return reverse('katalog', args=[self.id])


class Order(models.Model):
    '''Таблиця заказу'''
    user_name = models.CharField(max_length=50)
    user_surname = models.CharField(max_length=50)
    email = models.EmailField()
    address_post = models.CharField(max_length=100)
    total_price = models.IntegerField()
    order = models.CharField(max_length=200)
    is_made = models.BooleanField(default=False)

    def __str__(self):
        return self.order
