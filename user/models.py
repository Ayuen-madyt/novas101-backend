from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True, blank=True)
    image = models.ImageField(upload_to="profiles/", default="profile.png")
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'