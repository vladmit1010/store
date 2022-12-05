from django.urls import path
from . import views

urlpatterns = [
    path('show_puzzles', views.show_puzzles, name='show_puzzles'),
    path('show_companies/', views.show_companies, name='show_companies'),
    path('show_types/', views.show_types, name='show_types'),
    path('show_orders/', views.show_orders, name='show_orders'),
    path('add_puzzle/', views.add_puzzle, name='add_puzzle'),
    path('add_company/', views.add_company, name='add_company'),
    path('add_type/', views.add_type, name='add_type'),
    path('delete_puzzle/<int:id>', views.delete_puzzle, name='delete_puzzle'),
    path('delete_company/<int:id>', views.delete_company, name='delete_company'),
    path('delete_type/<int:id>', views.delete_type, name='delete_type'),
    path('delete_order/<int:id>', views.delete_order, name='delete_order'),
    path('edit_puzzle/<int:id>', views.edit_puzzle, name='edit_puzzle'),
    path('edit_company/<int:id>', views.edit_company, name='edit_company'),
    path('edit_type/<int:id>', views.edit_type, name='edit_type'),
    path('edit_order/<int:id>', views.edit_order, name='edit_order'),
]
