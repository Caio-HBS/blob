from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User


class Post(models.Model):
    """
    TODO: documentation.
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to="profile_pictures", blank=True, null=True)
    text = models.TextField(max_length=2000, blank=False, null=False)

    def __str__(self):
        return f'"{self.title} - By: {self.owner.username}"'

    def save(self, **kwargs):
        """
        TODO: documentation.
        """
        if not self.title:
            try:
                text_excert = self.text[50]
            except:
                text_excert = self.text[-1]
            else:
                raise ValidationError("Please provide a valid title.")
            self.title = text_excert

        super().save(**kwargs)


class Comments(models.Model):
    """
    TODO: documentation.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"{self.owner.username} in {self.related_post.title}"
