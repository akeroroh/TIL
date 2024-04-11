from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('nickname', )


class BookForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.filter(user=user)
    
    class Meta:
        model = Book
        fields = '__all__'


# class SomeModelForm(forms.ModelForm):
# 		# ModelForm 생성자 재정의
# 		# user 인자 추가 -> 추후 ModelForm 호출시 첫번째 인자로 넘길 값을 받을 변수
#     def __init__(self, user, *args, **kwargs):
# 				# 부모의 ModelForm의 생성자 실행
#         super(SomeModelForm, self).__init__(*args, **kwargs)
# 				# 1:N 관계를 맺을 필드 재정의
# 				# 필드에 노출될 queryset을 ModelForm 호출시 넘겨준 `user`를 기반으로 참조 대상 조회
#         self.fields['RelationModelFieldname'].queryset = RelationModel.objects.filter(user=user)
        
#     class Meta:
#         model = SomeModelForm
#         fields = '__all__'
