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
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author_profile')
    create_date = models.DateTimeField('프로필생성일', blank=True)
    images = models.ImageField('프로필 사진', blank=True, upload_to="images", null=True)
    birthdate = models.DateField('생년월일', blank=True)
    mbti = models.CharField('MBTI', max_length=50, blank=True, null=True)

    # workout html, forms, models 수정 요망
    workout = models.CharField('즐겨하는 스포츠', max_length=50, null=True, blank=True)
    Sport_type = models.CharField('관심 스포츠', max_length=50, null=True, blank=True)
    career = models.TextField('즐겨하는 운동 목표', max_length=50, null=True, blank=True)
    car_num = models.IntegerField('즐겨하는 운동 목표 달성도', null=True, blank=True)
    career2 = models.TextField('관심 운동 목표', max_length=50, null=True, blank=True)
    car_num2 = models.IntegerField('관심 운동 목표 달성도', null=True, blank=True)


    introduce = models.TextField('자기소개', max_length=500, null=True, blank=True)
    url = models.URLField('오픈채팅 url', null=True, blank=True)

