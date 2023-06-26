from django.contrib.auth.models import User
from django.db import models

class Posting(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_posting')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_posting')
    def __str__(self):
        return self.subject


# class Article(models.Model):
#     #article 테이블
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_article')
#     #제목
#     subject = models.CharField(max_length=200)
#     #모집 운동 종목
#     sport_type = models.CharField(max_length=20)
#     #모집 성별
#     gender = models.CharField(max_length=200)
#     #모집 상태
#     status = models.CharField(max_length=3)
#     #모집 지역
#     area = models.CharField(max_length=200)
#     #운동 할 날
#     sport_date = models.DateTimeField() #함수 참조 요망
#     #모집 내용
#     content =models.TextField()
#
#     create_date = models.DateTimeField()
#     #유저 테이블에 링크가된다 .
#     modify_date = models.DateTimeField(null=True,blank=True)
#     voter = models.ManyToManyField(User, related_name='voter_article') #voter추가
#     def __str__(self):
#         return self.subject

# class content(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_content')
#     question = models.ForeignKey(article, on_delete=models.CASCADE)
#     #ForeignKey는 외례키를 의미한다.
#     content = models.TextField()
#     create_date = models.DateTimeField()
#
#     #CASCADE는 계정이 삭제되면 연결된 모델도 삭제
#     modify_date = models.DateTimeField(null=True, blank=True)
#     voter = models.ManyToManyField(User,related_name='voter_content')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    posting = models.ForeignKey(Posting, null=True, blank=True, on_delete=models.CASCADE)
    # article = models.ForeignKey(Article, null=True,blank=True,on_delete=models.CASCADE)
    #answer = models.ForeignKey(content,null=True,blank=True,on_delete=models.CASCADE)

#수정중
# class pro(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#




