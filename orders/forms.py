from django import forms
from .models import orders_list

class orderhere(forms.ModelForm):
    class Meta:
        model = orders_list
        fields = ['product']