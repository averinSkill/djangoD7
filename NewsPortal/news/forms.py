# from django.forms import ModelForm, Textarea, Form
from django import forms
from .models import Post, Category


# Создаём модельную форму
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'type_post')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


# class CategorySubscribersForm(forms.Form):
#     category = forms.ModelChoiceField(queryset=Category.objects.all())

