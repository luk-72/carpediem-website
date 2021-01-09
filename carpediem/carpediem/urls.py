from django.urls import path

from home import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ex: /polls/
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)