from django import forms
from .models import TypePuzzle, Company

CHOICE_TYPE = ((type.name, type.name) for type in TypePuzzle.objects.all().order_by('name'))
CHOICE_COMPANY = ((company.name, company.name) for company in Company.objects.all().order_by('name'))


class PuzzleForm(forms.Form):
    type = forms.MultipleChoiceField(choices=CHOICE_TYPE, widget=forms.CheckboxSelectMultiple(), label='Тип')
    company = forms.MultipleChoiceField(choices=CHOICE_COMPANY, widget=forms.CheckboxSelectMultiple(), label='Бренды')
    price_from = forms.IntegerField(label='цена от',required=False)
    price_to = forms.IntegerField(label='цена до',required=False)
