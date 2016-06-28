from django import forms


class CityForm(forms.Form):
    name = forms.CharField(label='City name', max_length=100)


class StreetForm(forms.Form):
    name = forms.CharField(label='Street name', max_length=100)
    length = forms.IntegerField(label='Street length', min_value=0)


class SearchForm(forms.Form):
    city_name_search = forms.CharField(label='City name', max_length=50, required=False)
    street_name_search = forms.CharField(label='Street name', max_length=50, required=False)
