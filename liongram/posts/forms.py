from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Post

# class PostBaseForm(forms.Form):
#     CATEGORY_CHOICES = [
#         ('1', '일반'),
#         ('2', '계정'),
#     ]
#     image = forms.ImageField(label='이미지')
#     content = forms.CharField(label='내용', widget=forms.Textarea, required=True)
    # content = forms.CharField()
    # category = forms.ChoiceField(label='카테고리', choices=CATEGORY_CHOICES)

class PostBaseForm(forms.ModelForm):
    # modelForm을 상속받을 때에는 class를 하나 더 정리해 주어야 함
    class Meta:
        model = Post
        fields = '__all__'

from django.core.exceptions import ValidationError
class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']
        # 특정 항목만 노출하도록 설정함
    def clean_content(self):
        data = self.cleaned_data['content']
        if "비속어" == data:
            raise ValidationError("'비속어' 는 사용하실 수 없습니다.")
        return data

class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']

class PostDetailForm(PostBaseForm):
    pass
