from django import forms
from .models import Post, Comment


class CreatePost(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreatePost, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Заголовок'
        self.fields['title'].widget.attrs['class'] = 'title item__post__form'
        self.fields['title'].widget.attrs['placeholder'] = 'Заголовок'
        self.fields['text'].label = 'Текст'
        self.fields['text'].widget.attrs['class'] = 'text item__post__form'
        self.fields['text'].widget.attrs['placeholder'] = 'Текст'
        self.fields['file'].widget.attrs['class'] = 'upload__file'
        self.fields['img'].widget.attrs['class'] = 'upload__img'
        # self.fields['img'] = 'Изображение'

    class Meta:
        model = Post
        fields = ['title', 'text', 'img', 'file']


class CreateComment(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateComment, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['class'] = 'text__comment__form'
        self.fields['text'].widget.attrs['forms'] = 'Textarea'

    class Meta:
        model = Comment
        fields = ['text']

