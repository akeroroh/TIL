from django import forms
from .models import Menu
from django.core.exceptions import ValidationError

def validate_price(value):
    try:
        price = float(value)
    except ValueError:
        raise ValidationError('올바른 가격을 입력해 주세요. 예: 12.34')

    if len(value) > 8:
        raise ValidationError('가격은 최대 8자리여야 합니다.')

    if len(value.split('.')[-1]) > 2:
        raise ValidationError('가격은 소수점 이하 2자리여야 합니다.')

class MenuForm(forms.ModelForm):

    IS_VEGAN_CHOICES = (
    (True, 'Yes'),
    (False, 'No'),
    )

    is_vegan = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'is-vegan-radio'}),
        choices=IS_VEGAN_CHOICES,
        label='Is Vegan'
    )


    price = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '가격을 입력해 주세요.'}),
    validators=[validate_price]
    )

    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 이름을 작성해 주세요.'
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 설명을 작성해 주세요.'
                    }
                ),
            # 'is_vegan': forms.RadioSelect(
            #     attrs={
            #         'class': 'form-check-input',
            #     }
            # ),
        }
    
    def clean_is_vegan(self):
        is_vegan = self.cleaned_data.get('is_vegan')
        # Convert 'yes' to True and 'no' to False
        if is_vegan == 'yes':
            return True
        elif is_vegan == 'no':
            return False
        return is_vegan