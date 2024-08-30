from django import forms
from .models import Region, Bout





class CreateRegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['name','about']




class UpdateRegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['name', 'about']



