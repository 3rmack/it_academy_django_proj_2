from django import forms


class FirstForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    comment = forms.CharField(label='Comment', max_length=500)


class SecondForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    age = forms.IntegerField(label='Age', min_value=18, max_value=56)
    email = forms.EmailField(label='E-mail')
    tel_number = forms.IntegerField(label='Telephone number', max_value=9999999999999)
