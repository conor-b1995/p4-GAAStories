from .models import Comment, Post, ContactUs
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'excerpt',
            'featured_image',
        )


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = '__all__'
