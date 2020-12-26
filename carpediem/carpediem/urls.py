from django.urls import path

from home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
]