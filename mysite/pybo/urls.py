from django.urls import path
from .views import base_views,article_views,articleComment_views,vote_views

app_name = 'pybo'

urlpatterns =[
    path('article/list',base_views.main,name='main'),
    # 기존 path('article/list',base_views.article_index,name='main'),
    # 주소 명이랑 html 이름이랑 함수랑 다 헷갈리게 적혀 있습니다 ㅠㅠ
    # 혹시 문제 생길 시 여기 수정
    path('article/detail/<int:article_id>/',article_views.article_detail,name='article_detail'),
    path('article/create/',article_views.article_create,name='article_create'),
    path('article/index/',base_views.article_index,name='article_index'),
    path('article/modify/<int:article_id>/', article_views.article_modify, name='article_modify'),
    path('article/delete/<int:article_id>/',article_views.article_delete, name='article_delete'),
    #articleComment
    path('articleComment/create/article/<int:article_id>/', articleComment_views.articleComment_create_article, name='articleComment_create_article'),
    path('articleComment/modify/article/<int:articleComment_id>/', articleComment_views.articleComment_modify_article, name='articleComment_modify_article'),
    path('articleComment/deletearticle/<int:articleComment_id>/', articleComment_views.articleComment_delete_article, name='articleComment_delete_article'),
    path('articleComment/vote/<int:articleComment_id>/', vote_views.high_five, name='articleComment_high_five'),

]