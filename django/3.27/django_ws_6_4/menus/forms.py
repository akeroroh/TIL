from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '메뉴 이름을 작성해주세요'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '메뉴 설명을 작성해주세요'}),
        }

    # name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': '메뉴 이름을 작성해주세요'
    #         }
    #     )
    # )

    # price = forms.DecimalField(
    #     widget=forms.DecimalField(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     )
    # )

    # description = forms.CharField(
    #     widget = forms.Textarea(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': '메뉴 설명을 작성해주세요'
    #         }
    #     )
    # )