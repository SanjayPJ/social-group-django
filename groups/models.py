from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Group(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(blank=True, default=True)

    def __str__(self):
        return self.name

class GrupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
