from django.contrib import admin
from .models import Company, Puzzle, TypePuzzle


@admin.register(Puzzle)
class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('model', 'type', 'img')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(TypePuzzle)
class TypePuzzleAdmin(admin.ModelAdmin):
    pass