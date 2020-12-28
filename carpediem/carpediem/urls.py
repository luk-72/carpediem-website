from django.urls import path

from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ex: /polls/
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('team', views.team, name='team'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)