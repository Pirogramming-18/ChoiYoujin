from django import forms
from .models import Post

# django 안에 forms라는 라이브러리 사용

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'