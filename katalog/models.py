from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TypePuzzle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Puzzle(models.Model):
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
