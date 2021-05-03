from django import forms


class BrandSearchForm(forms.Form):
    search_keyword = forms.CharField(label='Search Keyword')
