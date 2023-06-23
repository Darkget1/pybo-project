from django.contrib import admin
from django.urls import path,include




urlpatterns = [
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('pybo/',include('pybo.urls')),
    # path('',base_views.index,name='index'),
    # path('pybo/')
]
