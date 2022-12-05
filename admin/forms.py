from django.forms import ModelForm

from katalog.models import Puzzle, Company, TypePuzzle, Order


class PuzzleForms(ModelForm):
    '''
    Форма для головоломок
    '''
    class Meta:
        model = Puzzle
        fields = ['type', 'model', 'company', 'img', 'price', 'counter']


class CompanyForms(ModelForm):
    '''
    Форма для компаній
    '''
    class Meta:
        model = Company
        fields = ['name', 'country']


class TypeForms(ModelForm):
    '''
    Форма для типів
    '''
    class Meta:
        model = TypePuzzle
        fields = ['name']


class OrderForms(ModelForm):
    '''
    Форма для заказів
    '''
    class Meta:
        model = Order
        fields = ['user_name', 'user_surname', 'email', 'address_post', 'total_price', 'order', 'is_made']
