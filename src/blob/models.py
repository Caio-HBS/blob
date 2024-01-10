import secrets

from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Represents a Post.

    Attributes:
        owner: the `User` to which the Post belongs;
        title: the title of the Post;
        image: the image for the Post (not required);
        text: the text for the Post;
        slug: the slug for the Post (provided automatically);
        time: the time the Post was made (provided automatically).
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="profile_pictures", blank=True, null=True)
    text = models.TextField(max_length=2000, blank=False, null=False)
    slug = models.SlugField(max_length=10, unique=True, blank=True, null=True)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'"{self.title} - By: {self.owner.username}"'

    def save(self, **kwargs):
        """
        Provides a title based on the text for the Post, as well as a unique slug.
        """
        if not self.title:
            try:
                text_excert = self.text[50]
            except:
                text_excert = self.text[-1]
            else:
                raise ValidationError("Please provide a valid title.")
            self.title = text_excert

        self.slug = secrets.token_urlsafe(7)[:7]

        super().save(**kwargs)


class Comments(models.Model):
    """
    A Comment instance for the Posts.

    Attributes:
        owner: the `User` that left the comment;
        related_post: the Post to which the comment was left;
        text: the text for the Comment;
        time: the time the Comment was made (provided automatically).
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=150, null=False, blank=False)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner.username} in {self.related_post.title}"
