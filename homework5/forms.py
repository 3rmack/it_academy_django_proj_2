from django import forms


class WorkerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    birth_year = forms.IntegerField()


class EquipmentForm(forms.Form):
    equipment_name = forms.CharField(max_length=100)
    inventory_id = forms.IntegerField()
    cost = forms.IntegerField()
