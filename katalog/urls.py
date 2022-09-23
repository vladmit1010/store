from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='katalog'),
    path('about/', views.about, name='about'),
    path('contact/', views.catalog, name='contact'),
    path('<int:id_puuzle>/', views.about_puzzle, ),
    path('filter/', views.filter, name='filter'),
]
