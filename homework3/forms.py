from django import forms


class DataForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    favourite_color = forms.CharField(label='Favourite Color', max_length=50)
    email = forms.EmailField(label='e-mail')
    height = forms.FloatField(label='Height', max_value=300, min_value=0)
    weight = forms.FloatField(label='Weight', min_value=0)


class SearchForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, required=False)
    favourite_color = forms.CharField(label='Favourite Color', max_length=50, required=False)
    email = forms.EmailField(label='e-mail', required=False)
    height = forms.FloatField(label='Height', max_value=300, min_value=0, required=False)
    weight = forms.FloatField(label='Weight', min_value=0, required=False)
