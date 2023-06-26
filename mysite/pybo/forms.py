from django import forms
from django.contrib.auth.forms import UserCreationForm
from pybo.models import Article

class ArticleForm(forms.ModelForm):

    subject = forms.(label='이메일')
    tel = forms.CharField(label='연락처')
    first_name = forms.CharField(label='성')
    last_name = forms.CharField(label='이름')
    gender = forms.CharField(label='성별')
    nickname = forms.CharField(label='닉네임')


    subject = forms.CharField(label='제목')
    #모집 운동 종목
    sport_type = forms.CharField(label='운동 종목')
    #모집 성별
    gender = forms.RadioSelect(label='모집 성별')
    #모집 상태
    status = forms.CharField(label='모집 상태')
    #모집 지역
    area = forms.CharField(label='운동 지역')
    #운동 할 날
    sport_date = forms.DateTimeField() #함수 참조 요망
    #모집 내용
    content =forms.Textarea(label='모집 내용')


    class Meta:
        model = Article
        fields = ("subject","sport_type","gender","status","area","sport_date","content")
