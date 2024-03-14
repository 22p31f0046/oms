from django import forms
from .models import productlist

class addproducts(forms.ModelForm):
    class Meta:
        model = productlist
        fields = ['title','tag','usage','price','rating']