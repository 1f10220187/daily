from django import forms
from .models import Daily,Comment

class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
       model = Comment
       fields = ['text']