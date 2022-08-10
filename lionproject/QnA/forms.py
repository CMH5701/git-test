from django import forms
from .models import Qna, Comment, Hashtag

class QnaForm(forms.ModelForm):
    class Meta:
        model = Qna
        fields = ['question','q_photo', 'hashtags']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']
