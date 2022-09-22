from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('katalog/', views.home, name='katalog'),
    path('about/', views.about, name='about'),
    path('contact/', views.catalog, name='contact'),
    path('katalog/<int:id_puuzle>', views.about_puzzle, ),
    path('filter', views.filter, name='filter'),
]
