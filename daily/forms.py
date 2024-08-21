from django import forms
from .models import Daily

class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['title', 'content']