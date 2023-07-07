from django import forms
from django.contrib.auth.models import User
from blog.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


