from django import forms
from .models import TypePuzzle, Company

CHOICE_TYPE = ((type.name, type.name) for type in TypePuzzle.objects.all().order_by('name'))
CHOICE_COMPANY = ((company.name, company.name) for company in Company.objects.all().order_by('name'))


class PuzzleForm(forms.Form):
    type = forms.MultipleChoiceField(choices=CHOICE_TYPE, widget=forms.CheckboxSelectMultiple())
    company = forms.MultipleChoiceField(choices=CHOICE_COMPANY, widget=forms.CheckboxSelectMultiple())
    price_from = forms.IntegerField(required=False)
    price_to = forms.IntegerField(required=False)
