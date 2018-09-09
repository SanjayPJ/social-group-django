from django.db import models
from django.contrib.auth import get_user_model
from groups.models import Group

# Create your models here.
User= get_user_model()

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField( auto_now=True)
    message = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.message

