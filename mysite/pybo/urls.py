from django.urls import path
from .views import base_views,article_views

app_name = 'pybo'

urlpatterns =[
    path('',base_views.main,name='main'),
    path('article/create/',article_views.article_create,name='article_create'),

]