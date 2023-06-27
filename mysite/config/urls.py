
from django.contrib import admin
from django.urls import path, include
from pybo import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('posting/', include('posting.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('', views.base_views.main, name='main'),
    # path('pybo/')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
