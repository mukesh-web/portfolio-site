from django import forms
from .models import Portfolio,Blog



class PortForm(forms.ModelForm):
    class Meta:
        model=Portfolio
        fields='__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['name','title','email','location','desc']