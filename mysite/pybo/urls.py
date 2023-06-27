from django.urls import path
from .views import base_views,article_views,articleComment_views

app_name = 'pybo'

urlpatterns =[
    path('',base_views.article_index,name='main'),
    path('article/detail/<int:article_id>/',article_views.article_detail,name='article_detail'),
    path('article/create/',article_views.article_create,name='article_create'),
    path('article/index/',base_views.article_index,name='article_index'),
    path('article/modify/<int:article_id>/', article_views.article_modify, name='article_modify'),
    path('article/delete/<int:article_id>/',article_views.article_delete, name='article_delete'),
    #articleComment
    path('articleComment/create/article/<int:article_id>/', articleComment_views.articleComment_create_article, name='articleComment_create_article'),
    path('articleComment/modify/article/<int:article_id>/', articleComment_views.articleComment_modify_article, name='articleComment_modify_article'),
    path('articleComment/deletearticle/<int:article_id>/', articleComment_views.articleComment_delete_article, name='articleComment_delete_article'),

]