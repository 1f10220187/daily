from django import forms
from .models import Daily,Comment

class DailyForm(forms.ModelForm):
    class Meta:
        model = Daily
        fields = ['title', 'content']
    
    def __init__(self, *args, **kwargs):
        super(DailyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class CommentForm(forms.ModelForm):
    class Meta:
       model = Comment
       fields = ['text']
      
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['text'].widget.attrs.update({
        'rows': '2',  # 縦の行数を減らす（例: 3行）
        'style': 'height: 70px;'  # 高さを具体的に指定する（例: 100px）
    })