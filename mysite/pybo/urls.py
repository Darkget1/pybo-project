from django.urls import path
from .views import base_views

app_name = 'pybo'

urlpatterns =[
    path('',base_views.main,name='main'),
]