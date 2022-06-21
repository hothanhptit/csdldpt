
from django import forms


class SearchForm(forms.Form):
    search = forms.ImageField(label='Query', required=True,
                              widget=forms.FileInput(attrs={'accept': 'image/*'}))
