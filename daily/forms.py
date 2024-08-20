from django import forms

class DailyForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(max_length=1000)
