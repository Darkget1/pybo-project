from django import forms
from django.contrib.auth.forms import UserCreationForm
from common.models import User, Profile

class UserForm(UserCreationForm):

    email = forms.EmailField(label='이메일')
    tel = forms.CharField(label='연락처')
    first_name = forms.CharField(label='성')
    last_name = forms.CharField(label='이름')
    gender = forms.CharField(label='성별')
    nickname = forms.CharField(label='닉네임')


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "tel", "gender", "nickname")

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profile_img','profile_img_date']
#         labels = {
#             'profile_img' :'프로필이미지',
#             'profile_img_date' : '프로필이미지저장날자',
#         }

class ProfileForm(forms.ModelForm):

    nickname = forms.CharField(label='닉네임')
    images = forms.ImageField(label='프로필 사진')
    img_date = forms.DateTimeField(label='프로필생성일')
    birthdate = forms.DateField(label='생년월일')
    mbti = forms.CharField(label='mbti 선택')
    workout = forms.CharField(label='관심운동')
    introduce = forms.CharField(label='자기소개')
    url = forms.URLField(label='오픈채팅 url')


    class Meta:
        model = Profile
        fields = ("nickname", "images", "img_date", "birthdate", "mbti", "workout", "introduce", "url")