from django import forms


class BuyerForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email = forms.EmailField()
    address_post = forms.CharField(max_length=200)
