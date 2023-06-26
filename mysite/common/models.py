from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    first_name = models.CharField("성", max_length=20, null=True, blank=True)
    last_name = models.CharField("이름", max_length=20, null=True, blank=True)
    tel = models.CharField("연락처", max_length=20, null=True, blank=True)
    gender = models.CharField('성별', max_length=20, null=True, blank=True)
    nickname = models.CharField('닉네임', max_length=20, null=True, blank=True)

class Profile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_profile')
    create_date = models.DateTimeField('프로필생성일')
    images = models.ImageField(blank=True, upload_to="images", null=True)





