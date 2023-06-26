from django.db import models
from common.models import User



class Article(models.Model):
    #article 테이블
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_article')
    #제목
    subject = models.CharField(max_length=200)
    #모집 운동 종목
    Sport_type = models.CharField(max_length=20)
    #모집 성별
    gender = models.CharField(max_length=3)
    #모집 상태
    status = models.CharField(max_length=10)
    #모집 지역
    area = models.CharField(max_length=200)
    #운동 할 날
    sport_date = models.DateTimeField() #함수 참조 요망
    #모집 내용
    content =models.TextField()

    create_date = models.DateTimeField()
    #유저 테이블에 링크가된다 .
    modify_date = models.DateTimeField(null=True,blank=True)
    voter = models.ManyToManyField(User,related_name='voter_article') #voter추가
    def __str__(self):
        return self.subject


class ArticleComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    article = models.ForeignKey(Article, null=True,blank=True,on_delete=models.CASCADE)








