from django import forms
from django.contrib.auth.forms import UserCreationForm
from pybo.models import Article,ArticleComment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =['subject','content','Sport_type','gender','status','area','sport_date']
        # widgets ={
        #     'subject':forms.TextInput(attrs={'class':'form-control'}),
        #     'content':forms.Textarea(attrs={'class':'form-control','rows':10}),
        # }
        labels ={
            'subject' : '제목',
            'content' : '내용',
            'Sport_type' : '운동 선택',
            'gender' : '성별',
            'status' : '모집상태',
            'area' : '모집지역',
            'sport_date' : '운동 할 날',


        }

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

    # #모집 운동 종목
    # sport_type = forms.CharField(label='운동 종목')
    # #모집 성별
    # gender = forms.RadioSelect(label='모집 성별')
    # #모집 상태
    # status = forms.CharField(label='모집 상태')
    # #모집 지역
    # area = forms.CharField(label='운동 지역')
    # #운동 할 날
    # sport_date = forms.DateTimeField() #함수 참조 요망
    # #모집 내용
    # content =forms.Textarea(label='모집 내용')
    #
    #
    # class Meta:
    #     model = Article
    #     fields = ("subject","sport_type","gender","status","area","sport_date","content")
