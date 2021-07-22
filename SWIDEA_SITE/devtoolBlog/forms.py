from django import forms
from .models import Devtool


class ToolForm(forms.ModelForm):
    class Meta:
        model = Devtool
        fields = '__all__'
