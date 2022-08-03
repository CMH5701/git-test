from django import forms
from .models import Blog, Comment, Hashtag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','image', 'hashtags']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']
