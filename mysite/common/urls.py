from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

from django.conf import settings
from django.conf.urls.static import static
app_name = 'common'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/create/', views.Profile, name='profile'),
    path('mypage/<int:profile_id>/', views.Profile_detail, name='mypage'),
    # path('profile/update/<int:profile_id>/', views.Profile_update, name='update'),
]
