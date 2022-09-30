from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='katalog'),
    path('about/', views.about, name='about'),
    path('contact/', views.catalog, name='contact'),
    path('<int:id_puzzle>/', views.about_puzzle, ),
    path('filter/', views.filter, name='filter'),

    path('my_basket/', views.my_basket, name='my_basket'),
    path('add_to_cart/<int:id_puzzle>', views.add_puzzle_to_cart, name='add_puzzle_to_cart'),
    path('remove_puzzle_in_basket/<int:id_puzzle>', views.remove_puzzle_in_basket, name='remove_puzzle_in_basket'),
]
