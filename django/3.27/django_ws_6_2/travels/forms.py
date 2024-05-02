from django import forms
from .models import Travels

class TravelsForm(forms.ModelForm):
    class Meta:
        model = Travels
        fields = '__all__'
        widgets = {
            'plan': forms.Textarea(attrs={'placeholder': 'ex) 슉.슈숙'}),
            'location': forms.TextInput(attrs={'placeholder': 'ex) 제주도'}),
            'start_date': forms.DateInput(attrs={'placeholder': 'ex) 2022-02-222'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'ex) 2022-02-22'}),
        }