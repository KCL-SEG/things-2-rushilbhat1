"""Forms of the project."""

# Create your forms here.

from django import forms
from .models import Thing


class ThingForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Thing 
        fields = ['name', 'description', 'quantity']


