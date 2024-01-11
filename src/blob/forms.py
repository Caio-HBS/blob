from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from blob.models import Post, Comments


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]

    def clean_title(self):
        title = self.cleaned_data["title"]

        if len(title) < 5:
            raise ValidationError("Title must be at least 5 characters long.")
        return title

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")

        if len(text) < 50:
            raise ValidationError("Text must be at least 50 characters long.")

        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")

        if len(text) == 0:
            raise ValidationError("You can't create a comment without text.")

        return cleaned_data