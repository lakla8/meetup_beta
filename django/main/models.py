from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Meet(models.Model):
    group_name = models.CharField(max_length=50)
    users = models.ManyToManyField(to=User)


class UserRecommend(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.SET_NULL, null=True)
    # тут будут рекомендации
